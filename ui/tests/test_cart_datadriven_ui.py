import pytest

@pytest.mark.parametrize("product_name", [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt"
])
def test_remove_item_from_cart(setup_all_pages, validation, product_name):
    login_page, inventory_page, cart_page, _ = setup_all_pages

    # Login
    inventory_page = login_page.perform_login("standard_user", "secret_sauce")

    # Add product
    inventory_page.add_product_to_cart(product_name)

    # Go to cart
    inventory_page.go_to_cart()

    # Validate item exists first
    validation.validate_item_in_cart(product_name)

    # Remove product
    cart_page.remove_product(product_name)

    # Validate item removed
    validation.validate_item_removed_from_cart(product_name)
