from ui.pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_icon = self.page.locator(".shopping_cart_link")

    def add_product_to_cart(self, product_name: str):
        # product = self.page.locator(f"text={product_name}")
        product = self.page.locator(".inventory_item").filter(has_text=product_name)
        add_button = product.locator("button:has-text('Add to cart')")
        self.click_element(add_button)

    def go_to_cart(self):
        self.click_element(self.cart_icon)
