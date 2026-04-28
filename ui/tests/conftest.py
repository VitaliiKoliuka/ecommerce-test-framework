import pytest
from playwright.sync_api import Page

from ui.pages.login_page import LoginPage
from ui.pages.inventory_page import InventoryPage
from ui.pages.cart_page import CartPage
from ui.pages.checkout_page import CheckoutPage

from utils.config import URL
from utils.utils import log_message, LogLevel
from utils.validation import AppValidation
from api.clients.auth_client import AuthClient
import logging

logger = logging.getLogger(__name__)


# Browser setup
@pytest.fixture()
def setup_playwright(playwright, request):
    headed = request.config.getoption("--headed", default=False)
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    try:
        yield page
    finally:
        log_message(logger, "closing browser", LogLevel.INFO)
        browser.close()


# Login page only (used for login tests)
@pytest.fixture()
def setup_login_page(setup_playwright: Page):
    login_page = LoginPage(setup_playwright)
    login_page.navigate_to(URL)
    login_page.accept_cookies_if_present()

    log_message(logger, f"navigate to {URL}", LogLevel.INFO)
    return login_page


# All pages (for E2E flows)
@pytest.fixture()
def setup_all_pages(setup_playwright: Page):
    page = setup_playwright

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.navigate_to(URL)
    login_page.accept_cookies_if_present()

    return login_page, inventory_page, cart_page, checkout_page


# Validation layer
@pytest.fixture()
def validation(setup_all_pages):
    return AppValidation(setup_all_pages)

@pytest.fixture()
def auth_client():
    return AuthClient()