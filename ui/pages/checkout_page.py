from ui.pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.first_name = self.page.locator("#first-name")
        self.last_name = self.page.locator("#last-name")
        self.postal_code = self.page.locator("#postal-code")
        self.continue_button = self.page.locator("#continue")
        self.success_message = self.page.locator(".complete-header")
        self.finish_button = self.page.locator("#finish")

    def fill_checkout_info(self, first, last, postal):
        self.type_text(self.first_name, first)
        self.type_text(self.last_name, last)
        self.type_text(self.postal_code, postal)
        self.click_element(self.continue_button)

    def finish_checkout(self):
        self.click_element(self.finish_button)