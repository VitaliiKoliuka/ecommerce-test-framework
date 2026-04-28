import allure
from playwright.sync_api import Page
from ui.pages.base_page import BasePage
from ui.pages.inventory_page import InventoryPage
from utils.utils import log_message, LogLevel, take_screenshot


class LoginPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.username_field = self.page.locator("[name = 'user-name']")
        self.password_field = self.page.locator("[name='password']")
        self.login_button = self.page.locator("[name = 'login-button']")
        self.error_message_locator = self.page.locator("[data-test='error']")

    def accept_cookies_if_present(self):
        cookie_button = self.page.get_by_role(
            "button", name="Allow all cookies"
        )

        try:
            if cookie_button.is_visible(timeout=3000):
                cookie_button.click()
        except Exception:
            # Cookie popup not present – safe to ignore
            pass

    def get_error_message(self, expected_error_message):
        return self.page.locator(
            f'//div[contains(text(), "{expected_error_message}")]'
        )

    @allure.step("login")
    def perform_login(self, username: str, password: str) -> InventoryPage | None:
        log_message(self.logger,"performing login",level=LogLevel.INFO)
        self.type_text(self.username_field, username)
        self.type_text(self.password_field, password)
        self.click_element(self.login_button)
        if self.login_button.is_visible():
            log_message(self.logger, "Login failed", level=LogLevel.ERROR)
            take_screenshot(self.page, "login_failed")
            return None

        return InventoryPage(self.page)