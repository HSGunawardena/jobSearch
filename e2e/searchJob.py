from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.linkedin.com/")
    page.get_by_label("Email or phone").click()
    page.get_by_label("Email or phone").fill("xx")
    page.get_by_label("Email or phone").press("Tab")
    page.get_by_label("Password", exact=True).fill("yy")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("link", name="Jobs", exact=True).click()
    page.get_by_role("combobox", name="Search by title, skill, or company").click()
    page.get_by_role("combobox", name="Search by title, skill, or company").fill("Senior QA Automation")
    page.get_by_role("combobox", name="City, state, or zip code").click()
    page.get_by_role("combobox", name="City, state, or zip code").fill("Worldwid")
    page.get_by_role("button", name="Worldwide").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
