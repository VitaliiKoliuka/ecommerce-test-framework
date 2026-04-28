from utils.api_client import APIClient
from api.routes import Routes

class CartClient(APIClient):

    def get_carts(self):
        return self.get(Routes.GET_ALL_CARTS)

    def get_cart_by_id(self, cart_id):
        endpoint = Routes.GET_CART_BY_ID.format(id=cart_id)
        return self.get(endpoint)

    def get_user_cart(self, user_id):
        endpoint = Routes.GET_USER_CART.format(userId=user_id)
        return self.get(endpoint)

    def create_cart(self, payload):
        return self.post(Routes.CREATE_CART, json=payload.to_dict())

    def update_cart(self, cart_id, payload):
        return self.put(Routes.UPDATE_CART.format(id=cart_id),
                        json=payload.to_dict())

    def delete_cart(self, cart_id):
        endpoint = Routes.DELETE_CART.format(id=cart_id)
        return self.get(endpoint)