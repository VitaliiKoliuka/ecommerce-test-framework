from playwright.sync_api import expect
from ui.pages.base_page import BasePage
from utils.utils import take_screenshot, log_message, LogLevel


class AppValidation(BasePage):
    def __init__(self, setup_all_pages):
        (
            self.login_page,
            self.inventory_page,
            self.cart_page,
            self.checkout_page,
        ) = setup_all_pages

        super().__init__(self.login_page.page)



    def validate_logged_in(self):
        login_button = self.login_page.login_button
        try:
            expect(login_button).not_to_be_visible(), "failed to login"
        except Exception as e:
            log_message(self.logger,"login failed", LogLevel.ERROR)
            take_screenshot(self.page, "login failed")
            raise AssertionError("Login failed") from e


    def validate_failed_login(self, expected_error_message):
        login_button = self.login_page.login_button
        error_locator = self.login_page.error_message_locator

        try:
            expect(login_button).to_be_visible(), "login button was expected to be hidden, but it was visible"
            expect(error_locator).to_be_visible()
            expect(error_locator).to_contain_text(expected_error_message)
        except Exception as e:
            log_message(self.logger,"login validation failed", LogLevel.ERROR)
            take_screenshot(self.page, "login_failed")
            raise AssertionError(
                "Expected login button to be visible after failed login"
            ) from e

    def validate_order_success(self):
        success_message = self.checkout_page.success_message

        try:
            expect(success_message).to_be_visible()
            expect(success_message).to_have_text("Thank you for your order!")
        except Exception as e:
            log_message(self.logger, "order validation failed", LogLevel.ERROR)
            take_screenshot(self.page, "order_failed")
            raise AssertionError("Order was not completed successfully") from e


    def validate_item_removed_from_cart(self, product_name):
        product = self.cart_page.page.locator(".cart_item").filter(has_text=product_name)

        try:
            expect(product).to_have_count(0)
        except Exception as e:
            log_message(self.logger, "item was not removed from cart", LogLevel.ERROR)
            take_screenshot(self.page, "remove_item_failed")
            raise AssertionError(f"{product_name} was not removed from cart") from e

    def validate_cart_badge(self, expected_count: str):
        badge = self.page.locator(".shopping_cart_badge")
        expect(badge).to_be_visible()
        expect(badge).to_have_text(expected_count)

    def validate_item_in_cart(self, product_name):
        item = self.cart_page.page.locator(".cart_item").filter(has_text=product_name)
        expect(item).to_have_count(1)





