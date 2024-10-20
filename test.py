import time

import pytest
from playwright.sync_api import Page, expect


def test_view_all_data(page: Page):
    page.goto("https://oldtest.bumblebeeeee.com/login")
    page.get_by_role("textbox", name="username").fill("tester")
    page.get_by_role("textbox", name="password").fill("Raqz3Ts0D2fN")
    page.get_by_role("button", name="Log in").click()
    page.get_by_placeholder("Search").fill("test")
    expect(page.get_by_role("progressbar")).to_have_count(2)
    expect(page.get_by_role("progressbar")).to_have_count(0)
    page.get_by_role("button", name="See All Data").click()
    expect(page.get_by_role('gridcell')).to_be_enabled(timeout=100000)


@pytest.mark.skip
def test_login(page: Page):
    page.goto("https://oldtest.bumblebeeeee.com/login")
    page.get_by_role("textbox", name="username").fill("tester")
    page.get_by_role("textbox", name="password").fill("Raqz3Ts0D2fN")
    page.get_by_role("button", name="Log in").click()
    expect(page.get_by_placeholder("Search")).to_be_visible(timeout=10000)
