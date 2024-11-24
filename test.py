import time

import mailslurp_client
import pytest
from playwright.sync_api import Page, expect

from testData import TestData


@pytest.mark.skip("system doesn't send otp email")
def test_register(page: Page):
    page.goto("https://oldtest.bumblebeeeee.com/login")
    page.get_by_text("Create an account").click()
    # inbox, wait_for_controller = TestData.create_new_email_inbox()
    configuration = mailslurp_client.Configuration()  # create a mail-slurp configuration
    configuration.api_key['x-api-key'] = "9c9f1a5e8203d8db15ff02b7a60b315fb6b14f4036c42d538b26a9a87debfce4"
    api_client = mailslurp_client.ApiClient(configuration)  # create a mail-slurp client
    wait_for_controller = mailslurp_client.WaitForControllerApi(api_client)
    page.get_by_placeholder("Email").fill("8e5f0004-469c-412d-8fbf-a353f7eb0b05@mailslurp.biz")
    page.get_by_placeholder("Password").fill(TestData.new_account_password)
    page.get_by_role("button", name="Register").click()
    email_content = wait_for_controller.wait_for_latest_email(inbox_id="8e5f0004-469c-412d-8fbf-a353f7eb0b05",
                                                              timeout=30000)
    otp = TestData.get_otp_from_email_content(email_content.body)
    print(otp)
    time.sleep(5)


@pytest.mark.skip
def test_view_all_data(page: Page):
    page.goto("https://oldtest.bumblebeeeee.com/login")
    page.get_by_role("textbox", name="username").fill("tester")
    page.get_by_role("textbox", name="password").fill("Raqz3Ts0D2fN")
    page.get_by_role("button", name="Log in").click()
    page.get_by_placeholder("Search").fill("test")
    expect(page.get_by_role("progressbar")).to_have_count(2)
    expect(page.get_by_role("progressbar")).to_have_count(0)
    page.get_by_role("button", name="See All Data").click()
    e = page.get_by_role('gridcell')
    expect(e).to_have_count(292)


@pytest.mark.skip
def test_login(page: Page):
    page.goto("https://oldtest.bumblebeeeee.com/login")
    page.get_by_role("textbox", name="username").fill("tester")
    page.get_by_role("textbox", name="password").fill("Raqz3Ts0D2fN")
    page.get_by_role("button", name="Log in").click()
    expect(page.get_by_placeholder("Search")).to_be_visible(timeout=10000)


@pytest.mark.skip
def test_update_profile(page: Page):
    page.goto("https://oldtest.bumblebeeeee.com/login")
    page.get_by_role("textbox", name="username").fill("77c2beda-9176-41a9-8fc2-397ceb07cb7c@mailslurp.biz")
    page.get_by_role("textbox", name="password").fill("P@ssw0rd")
    page.get_by_role("button", name="Log in").click()
    page.get_by_text("yahia.soliman").click()
    page.get_by_label("User Menu").click()
    page.get_by_text("profile").click()
    page.get_by_role("textbox").first.fill("yahiaTester")
    page.get_by_role("textbox").nth(1).fill("yahia")
    page.get_by_role("textbox").nth(2).fill("soliman")
    page.get_by_role("textbox").nth(3).fill("QA")
    page.get_by_label("Go Back").click()
    page.get_by_label("User Menu").click()
    expect(page.get_by_role("menu")).to_contain_text("yahiaTester")
    time.sleep(5)
