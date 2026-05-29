import { expect, test, type APIRequestContext, type Page } from "@playwright/test";

const galleryRoutes = [
  {
    cta: /view all working groups/i,
    heading: /working groups/i,
    path: "/directory/working-groups/",
  },
  {
    cta: /view all projects/i,
    heading: /staff, postdoc & graduate research/i,
    path: "/directory/research/",
  },
  {
    cta: /view all events/i,
    heading: /events & summits/i,
    path: "/directory/events/",
  },
  {
    cta: /browse infrastructure/i,
    heading: /infrastructure & tools/i,
    path: "/directory/infrastructure/",
  },
] as const;

function isSkippableHref(href: string): boolean {
  return (
    href.startsWith("mailto:") ||
    href.startsWith("tel:") ||
    href.startsWith("javascript:")
  );
}

async function collectUniqueHrefs(page: Page, selector: string): Promise<string[]> {
  const hrefs = await page.locator(selector).evaluateAll((links) =>
    links
      .map((link) => link.getAttribute("href") || "")
      .filter((href) => href.length > 0),
  );

  return [...new Set(hrefs)].filter((href) => !isSkippableHref(href));
}

async function assertLinksResolve(
  page: Page,
  request: APIRequestContext,
  hrefs: string[],
) {
  const baseUrl = page.url();

  for (const href of hrefs) {
    if (href.startsWith("#")) {
      await expect(page.locator(href), `Missing same-page anchor target for ${href}`).toHaveCount(1);
      continue;
    }

    const resolved = new URL(href, baseUrl);
    const hash = resolved.hash;
    resolved.hash = "";

    const response = await request.get(resolved.toString(), {
      failOnStatusCode: false,
      maxRedirects: 5,
      timeout: 30000,
    });

    expect(
      response.status(),
      `Expected ${href} to resolve successfully, got ${response.status()} for ${resolved.toString()}`,
    ).toBeLessThan(400);

    if (hash && resolved.origin === new URL(baseUrl).origin) {
      const probe = await page.context().newPage();
      await probe.goto(resolved.toString());
      await expect(
        probe.locator(hash),
        `Missing hash target ${hash} on ${resolved.toString()}`,
      ).toHaveCount(1);
      await probe.close();
    }
  }
}

async function assertGalleryImagesResolve(page: Page, request: APIRequestContext) {
  const rawSources = await page
    .locator(".oasis-homepage img[src], .oasis-section-page img[src]")
    .evaluateAll((images) =>
      images
        .map((image) => image.getAttribute("src") || "")
        .filter((src) => src.length > 0),
    );

  const uniqueSources = [...new Set(rawSources)].filter((src) => !src.startsWith("data:"));

  for (const src of uniqueSources) {
    const resolved = new URL(src, page.url());
    const response = await request.get(resolved.toString(), {
      failOnStatusCode: false,
      maxRedirects: 5,
      timeout: 30000,
    });

    expect(
      response.status(),
      `Expected image source ${src} to resolve successfully, got ${response.status()} for ${resolved.toString()}`,
    ).toBeLessThan(400);
  }
}

test("homepage renders the custom OASIS layout", async ({ page }) => {
  await page.goto("/");

  await expect(page.locator(".oasis-homepage")).toBeVisible();
  await expect(
    page.getByRole("heading", {
      level: 1,
      name: /open analysis and synthesis infrastructure for science/i,
    }),
  ).toBeVisible();

  for (const sectionId of [
    "#working-groups-section",
    "#research-projects-section",
    "#events-summits-section",
    "#infrastructure-libraries-section",
  ]) {
    await expect(page.locator(sectionId)).toHaveCount(1);
  }

  await expect(page.getByRole("link", { name: /explore projects/i })).toHaveAttribute(
    "href",
    /#working-groups-section$/,
  );
  await expect(page.getByRole("link", { name: /browse libraries/i })).toHaveAttribute(
    "href",
    /#infrastructure-libraries-section$/,
  );
});

test("homepage band links open dedicated gallery pages and browser back returns home", async ({ page }) => {
  for (const route of galleryRoutes) {
    await page.goto("/");
    await expect(page.locator(".oasis-homepage")).toBeVisible();

    await page.getByRole("link", { name: route.cta }).click();

    await expect(page).toHaveURL(new RegExp(`${route.path.replace(/\//g, "\\/")}$`));
    await expect(page.locator(".oasis-section-page")).toBeVisible();
    await expect(page.getByRole("heading", { level: 1, name: route.heading })).toBeVisible();

    await page.goBack();

    await expect(page).toHaveURL(/\/$/);
    await expect(page.locator(".oasis-homepage")).toBeVisible();
    await expect(
      page.getByRole("heading", {
        level: 1,
        name: /open analysis and synthesis infrastructure for science/i,
      }),
    ).toBeVisible();
  }
});

test("gallery pages keep history intact through the directory hub", async ({ page }) => {
  await page.goto("/");
  await page.getByRole("link", { name: /view all working groups/i }).click();

  await expect(page).toHaveURL(/\/directory\/working-groups\/$/);
  await expect(page.getByRole("heading", { level: 1, name: /working groups/i })).toBeVisible();

  await page.getByRole("link", { name: /ecosystem directory/i }).click();
  await expect(page).toHaveURL(/\/directory\/$/);
  await expect(page.getByRole("heading", { level: 1, name: /ecosystem directory/i })).toBeVisible();

  await page.goBack();
  await expect(page).toHaveURL(/\/directory\/working-groups\/$/);
  await expect(page.locator(".oasis-section-page")).toBeVisible();

  await page.goBack();
  await expect(page).toHaveURL(/\/$/);
  await expect(page.locator(".oasis-homepage")).toBeVisible();
});

test("homepage and gallery links stay healthy", async ({ page, request }) => {
  test.slow();

  const routes = [
    "/",
    "/directory/",
    "/directory/working-groups/",
    "/directory/research/",
    "/directory/events/",
    "/directory/infrastructure/",
  ];

  for (const route of routes) {
    await page.goto(route);

    if (route === "/") {
      await expect(page.locator(".oasis-homepage")).toBeVisible();
    } else {
      await expect(page.locator(".oasis-section-page")).toBeVisible();
    }

    await assertGalleryImagesResolve(page, request);

    const hrefs = await collectUniqueHrefs(
      page,
      ".oasis-homepage a[href], .oasis-section-page a[href]",
    );
    await assertLinksResolve(page, request, hrefs);
  }
});
