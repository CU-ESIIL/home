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

async function assertNoHorizontalOverflow(page: Page, selector: string) {
  const metrics = await page.locator(selector).evaluate((root) => {
    const viewportWidth = document.documentElement.clientWidth;
    const scrollWidth = document.documentElement.scrollWidth;

    const offenders = Array.from(root.querySelectorAll("*"))
      .map((node) => {
        const rect = node.getBoundingClientRect();
        const text = (node.textContent || "").trim().replace(/\s+/g, " ").slice(0, 60);

        if (rect.width === 0 || rect.height === 0) {
          return null;
        }

        if (rect.left < -1 || rect.right > viewportWidth + 1) {
          return {
            tag: node.tagName.toLowerCase(),
            className: node.className,
            text,
            left: Math.round(rect.left),
            right: Math.round(rect.right),
          };
        }

        return null;
      })
      .filter(Boolean)
      .slice(0, 10);

    return { viewportWidth, scrollWidth, offenders };
  });

  expect(
    metrics.scrollWidth,
    `Expected ${selector} to avoid horizontal overflow, but document scrollWidth was ${metrics.scrollWidth} for viewport ${metrics.viewportWidth}. Offenders: ${JSON.stringify(metrics.offenders)}`,
  ).toBeLessThanOrEqual(metrics.viewportWidth + 1);
}

test("homepage renders the custom OASIS layout", async ({ page }) => {
  await page.goto("/");

  await expect(page.locator(".oasis-homepage")).toBeVisible();
  await expect(page.locator(".md-header__source")).toBeHidden();
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

  const statsBand = page.locator(".oasis-stats-band");
  await expect(statsBand).toBeVisible();
  await expect(
    statsBand.getByRole("heading", { name: /esiil science at scale/i }),
  ).toBeVisible();
  await expect(statsBand.getByText("Millions")).toBeVisible();
  await expect(statsBand.getByText("Compute Hours")).toBeVisible();
  await expect(statsBand.getByText(/github actions/i)).toHaveCount(0);
  await expect(
    page.locator(".oasis-home__hero + .oasis-stats-band + .oasis-interlude--data-insight"),
  ).toHaveCount(1);

  const heroQuicklinks = page.locator(".oasis-home__hero-quicklinks");

  await expect(heroQuicklinks.getByRole("link", { name: /quick start/i })).toHaveAttribute(
    "href",
    /\/quickstart\/$/,
  );
  await expect(
    heroQuicklinks.getByRole("link", { name: /i'm here for a training/i }),
  ).toHaveAttribute(
    "href",
    /\/trainings\/$/,
  );
  await expect(heroQuicklinks.getByRole("link", { name: /data library/i })).toHaveAttribute(
    "href",
    /https:\/\/cu-esiil\.github\.io\/data-library\/?$/,
  );
  await expect(
    heroQuicklinks.getByRole("link", { name: /analytics library/i }),
  ).toHaveAttribute(
    "href",
    /https:\/\/cu-esiil\.github\.io\/analytics-library\/?$/,
  );
  await expect(
    heroQuicklinks.getByRole("link", { name: /cloud container/i }),
  ).toHaveAttribute(
    "href",
    /\/quickstart\/cloud\/$/,
  );
  await expect(
    heroQuicklinks.getByRole("link", { name: /how to contribute/i }),
  ).toHaveAttribute(
    "href",
    /https:\/\/cu-esiil\.github\.io\/how_to_contribute\/?$/,
  );
});

test("theme toggle switches to dark mode without restoring the repo badge", async ({ page }) => {
  await page.goto("/");

  await expect(page.locator(".oasis-homepage")).toBeVisible();
  await expect(page.locator(".md-header__source")).toBeHidden();

  const themeToggle = page.locator('[data-md-component="palette"] label').first();
  await expect(themeToggle).toBeVisible();
  await themeToggle.click();

  await expect(page.locator("body")).toHaveAttribute("data-md-color-scheme", "slate");

  const headerBackground = await page.locator(".md-header").evaluate((node) =>
    window.getComputedStyle(node).backgroundColor,
  );
  expect(headerBackground).not.toBe("rgb(255, 255, 255)");

  await page.goto("/directory/working-groups/");
  await expect(page.locator(".oasis-section-page")).toBeVisible();
  await expect(page.locator("body")).toHaveAttribute("data-md-color-scheme", "slate");
  await expect(page.locator(".md-header__source")).toBeHidden();
});

test("homepage stays within the viewport on small screens", async ({ page }) => {
  await page.setViewportSize({ width: 320, height: 740 });
  await page.goto("/");

  await expect(page.locator(".oasis-homepage")).toBeVisible();
  await expect(
    page.getByRole("heading", {
      level: 1,
      name: /open analysis and synthesis infrastructure for science/i,
    }),
  ).toBeVisible();

  await assertNoHorizontalOverflow(page, ".oasis-homepage");
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
