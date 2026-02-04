from playwright.sync_api import expect
from time import sleep

def test_run(page):
    page.goto("https://www.baidu.com/")

    print("问文心元素是否存在：")
    expect(page.locator("#left-tool svg")).to_be_visible()

    print("点击输入框")
    page.locator("#chat-textarea").click()

    print("输入你好")
    page.locator("#chat-textarea").fill("你好")

    sleep(2)
    page.get_by_role("button", name="百度一下").click()
    sleep(2)

    page.go_back()
    sleep(2)
