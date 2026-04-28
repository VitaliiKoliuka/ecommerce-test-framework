from ui.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = self.page.locator("#checkout")
        self.cart_items = self.page.locator(".cart_item")

    def remove_product(self, product_name: str):
        product = self.page.locator(".cart_item").filter(has_text=product_name)
        remove_button = product.locator("button:has-text('Remove')")
        self.click_element(remove_button)

    def click_checkout(self):
        self.click_element(self.checkout_button)

    def get_cart_items(self):
        return self.cart_items