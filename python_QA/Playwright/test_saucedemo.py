from playwright.sync_api import Page
import pytest

#def test_title(page: Page):
    #page.goto("https://www.saucedemo.com/")
    #assert page.title() == "Swag Labs"

#def test_inventory_site(page: Page):
    #page.goto("https://www.saucedemo.com/inventory.html")
    #assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."

#Test run: pytest --headed --base-url https://www.saucedemo.com/ --browser chromium --browser firefox

@pytest.mark.skip_browser("chromium")
def test_title(page: Page):
    page.goto("/")
    assert page.title() == "Swag Labs"

def test_inventory_site(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."
