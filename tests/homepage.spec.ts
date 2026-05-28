import { expect, test, type APIRequestContext, type Page } from "@playwright/test";

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

test("homepage renders the custom OASIS layout", async ({ page }) => {
  await page.goto("/");

  await expect(page.locator(".oasis-homepage")).toBeVisible();
  await expect(page.getByRole("heading", { level: 1, name: /open analysis and synthesis infrastructure for science/i })).toBeVisible();

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

test("homepage and ecosystem directory links stay healthy", async ({ page, request }) => {
  test.slow();

  await page.goto("/");
  await expect(page.locator(".oasis-homepage")).toBeVisible();

  const homepageHrefs = await collectUniqueHrefs(page, ".oasis-homepage a[href]");
  await assertLinksResolve(page, request, homepageHrefs);

  await page.goto("/directory/");
  await expect(page.getByRole("heading", { level: 1, name: /ecosystem directory/i })).toBeVisible();

  const directoryHrefs = await collectUniqueHrefs(page, ".md-content__inner a[href]");
  await assertLinksResolve(page, request, directoryHrefs);
});
