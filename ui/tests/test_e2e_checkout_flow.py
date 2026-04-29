
def test_checkout_flow(setup_all_pages, validation):
    login_page, inventory_page, cart_page, checkout_page = setup_all_pages

    inventory_page = login_page.perform_login("standard_user", "secret_sauce")

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.fill_checkout_info("John", "Doe", "12345")
    checkout_page.finish_checkout()

    validation.validate_order_success()