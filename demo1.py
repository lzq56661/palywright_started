import re
from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://cas.arcsoft.com.cn:9443/cas/login?service=https://doc.arcsoft.com.cn/confirm_cas.asp?RedirectURL=")
    page.get_by_role("textbox", name="用户名:*").click()
    page.get_by_role("textbox", name="用户名:*").fill("123456")
    page.get_by_role("textbox", name="密 码:* 󰈈 Toggle Password").click()
    page.get_by_role("textbox", name="密 码:* 󰈈 Toggle Password").fill("123456")
    page.get_by_role("button", name="󰈈 Toggle Password").click()
    page.get_by_role("button", name="登  录").click()
    sleep(2)
    page.get_by_role("button", name="关闭").click()
    sleep(10)

    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
