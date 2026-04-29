from utils.api_client import APIClient
from api.routes import Routes
from dataclasses import asdict

class ProductClient(APIClient):

    def get_all_products(self):
        return self.get(Routes.GET_ALL_PRODUCTS)

    def get_single_product(self, product_id):
        endpoint = Routes.GET_PRODUCT_BY_ID.format(id=product_id)
        return self.get(endpoint)

    def get_limited_products(self, limit):
        endpoint = Routes.GET_PRODUCTS_WITH_LIMIT.format(limit=limit)
        return self.get(endpoint)

    def get_sorted_products_desc(self):
        endpoint = Routes.GET_PRODUCTS_SORTED.format(order="desc")
        return self.get(endpoint)

    def get_sorted_products_asc(self):
        endpoint = Routes.GET_PRODUCTS_SORTED.format(order="asc")
        return self.get(endpoint)

    def get_all_products_all_categories(self):
        endpoint = Routes.GET_ALL_CATEGORIES
        return self.get(endpoint)

    def get_products_by_categories(self, category):
        endpoint = Routes.GET_PRODUCTS_BY_CATEGORY.format(category=category)
        return self.get(endpoint)

    def create_product(self, payload):
        return self.post(Routes.CREATE_PRODUCT, json=asdict(payload))

    def update_product(self, product_id, payload):
        return self.put(
            Routes.UPDATE_PRODUCT.format(id=product_id),
            json=payload.__dict__
        )

    def delete_product(self, product_id):
        endpoint = Routes.DELETE_PRODUCT.format(id=product_id)
        return self.delete(endpoint)