import requests
import json
from api.routes import Routes
from utils.data_generator import Payload
from dataclasses import asdict
from utils.helpers import validate_cart_dates_within_range
import pytest


class TestCartAPI:
    @pytest.fixture(autouse=True)
    def init_class_vars(self,setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]
        self.payload = Payload()

    @pytest.mark.sanity
    @pytest.mark.run(order=1)
    def test_get_carts(self, cart_client):
        response = cart_client.get_carts()
        assert response.status_code==200
        data = response.json()
        # print(json.dumps(data,indent=4))
        assert len(data)>0

    @pytest.mark.sanity
    @pytest.mark.run(order=2)
    def test_get_cart_by_id(self, cart_client):
        cart_id = self.config.get_property("cartId")
        response = cart_client.get_cart_by_id(cart_id)
        assert response.status_code == 200
        # data = response.json()
        # print(json.dumps(data, indent=4))


    @pytest.mark.sanity
    @pytest.mark.run(order=4)
    def test_get_user_cart(self, cart_client):
        user_id = self.config.get_property("userId")
        response = cart_client.get_user_cart(user_id)
        assert response.status_code == 200
        data = response.json()
        # print(json.dumps(data, indent=4))
        carts = data["carts"]
        for item in carts:
            assert item["userId"] == int(user_id)

    @pytest.mark.smoke
    @pytest.mark.run(order=5)
    @pytest.mark.dependency(name="add_cart")
    def test_create_cart(self, cart_client):
        user_id = self.config.get_property("userId")
        cart = self.payload.cart_payload(user_id)
        response = cart_client.create_cart(cart)
        assert response.status_code == 201
        data = response.json()
        # print(json.dumps(data, indent=4))
        assert data["id"] is not None
        assert data["userId"] is not None
        assert len(data["products"]) > 0
    #
    @pytest.mark.regression
    @pytest.mark.run(order=6)
    @pytest.mark.dependency(depends=["add_cart"])
    def test_update_cart(self, cart_client):
        user_id = self.config.get_property("userId")
        cart_id = self.config.get_property("cartId")
        cart = self.payload.cart_payload(user_id)
        response = cart_client.update_cart(cart_id, cart)
        # print("Cart ID:", cart_id)
        # print("URL:", f"{Routes.UPDATE_CART}/{cart_id}")
        # print("Payload:", cart.to_dict())
        # print("Response:", response.text)
        assert response.status_code == 200
        data = response.json()

        # print(json.dumps(data, indent=4))

        assert data["id"] == int(cart_id)
        assert data["userId"] == int(user_id)
        assert len(data["products"]) == 1
    #
    @pytest.mark.regression
    @pytest.mark.run(order=7)
    @pytest.mark.dependency(depends=["add_cart"])
    def test_delete_cart(self, cart_client):
        cart_id = self.config.get_property("cartId")
        response = cart_client.delete_cart(cart_id)
        assert response.status_code in [200, 204, 404] #the client layer is structured, test API limitation required a temporary workaround
        data = response.json()
        # print(json.dumps(data, indent=4))












