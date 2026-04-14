import { expect, test } from "@playwright/test";

test("homepage key interactions work", async ({ page }) => {
  await page.goto("/");

  const topButtons = [
    { label: "Quickstart", type: "internal", path: /\/quickstart\/$/ },
    { label: "Containers", type: "internal", path: /\/container-library\/$/ },
    { label: "Analytics", type: "external", href: "https://cu-esiil.github.io/analytics-library/" },
    { label: "Data Library", type: "external", href: "https://cu-esiil.github.io/data-library/" },
    { label: "Resources", type: "internal", path: /\/resources\/$/ },
  ] as const;

  for (const button of topButtons) {
    const link = page.locator(".tag-suggestions").getByRole("link", { name: button.label });
    await expect(link).toBeVisible();
    const href = await link.getAttribute("href");
    expect(href).not.toBeNull();

    if (button.type === "external") {
      expect(href).toBe(button.href);
      continue;
    }

    await link.click();
    await expect(page).toHaveURL(button.path);
    await page.goBack();
  }

  const quickstartButton = page.locator(".quickstart-btn");
  await expect(quickstartButton).toBeVisible();
  await quickstartButton.click();
  await expect(page).toHaveURL(/\/quickstart\/$/);
  await page.goBack();

  for (const selector of [
    ".oasis-main .library-item a",
    ".oasis-main .gallery-item a",
    ".oasis-main .template-item a",
  ]) {
    const links = page.locator(selector);
    const limit = Math.min(3, await links.count());

    for (let index = 0; index < limit; index += 1) {
      const link = links.nth(index);
      await expect(link).toBeVisible();
      const href = await link.getAttribute("href");
      expect(href).toBeTruthy();
    }
  }

  const sidebarTagsLink = page.locator(".md-sidebar").getByRole("link", { name: "Tags" }).first();
  if (await sidebarTagsLink.isVisible()) {
    await sidebarTagsLink.click();
    await expect(page).toHaveURL(/\/tags\/$/);
  }
});
