import requests
import pytest
import json
from api.routes import Routes
from utils.data_generator import Payload

class TestProductAPI:
    @pytest.fixture(autouse=True)
    def init_class_vars(self,setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]
        # self.category = "jewelery"
        self.payload = Payload().product_payload()

    @pytest.mark.run(order=1)
    def test_get_products(self, product_client):
        response = product_client.get_all_products()
        assert response.status_code == 200
        data = response.json()
        assert len(data)>0
    #
    @pytest.mark.sanity
    @pytest.mark.run(order=2)
    def test_get_single_product_by_id(self, product_client):
        product_id = self.config.get_property("productId")
        response = product_client.get_single_product(product_id)
        assert response.status_code == 200

    @pytest.mark.sanity
    @pytest.mark.run(order=3)
    def test_get_limited_products(self, product_client):
        limit = self.config.get_property("limit")
        response = product_client.get_limited_products(limit)
        assert response.status_code == 200
        data = response.json()
        # print(json.dumps(data, indent=4))
        assert len(data) == int(limit)


    @pytest.mark.run(order=4)
    def test_get_sorted_products_desc(self, product_client):
        response = product_client.get_sorted_products_desc()
        assert response.status_code == 200
        data = response.json()
        # print(json.dumps(data, indent=4))
        products = response.json()["products"]
        prices = [item["price"] for item in products]

        assert prices == sorted(prices, reverse=True)

    @pytest.mark.run(order=5)
    def test_get_sorted_products_asc(self, product_client):
        response = product_client.get_sorted_products_asc()
        assert response.status_code == 200
        data = response.json()
        # print(json.dumps(data, indent=4))
        products = response.json()["products"]
        prices = [item["price"] for item in products]

        assert prices == sorted(prices)

    @pytest.mark.run(order=6)
    def test_get_all_products_all_categories(self, product_client):
        response = product_client.get_all_products_all_categories()
        assert response.status_code == 200
        # data = response.json()
        # print(json.dumps(data, indent=4))

    @pytest.mark.run(order=7)
    def test_get_products_by_categories(self, product_client):
        category=self.config.get_property("category")
        response = product_client.get_products_by_categories(category)
        assert response.status_code == 200
        # data = response.json()
        # print(json.dumps(data, indent=4))

    @pytest.mark.run(order=8)
    @pytest.mark.dependency(name="add_product")
    def test_create_product(self, product_client):
        response = product_client.create_product(self.payload)
        assert response.status_code == 201
        data = response.json()
        # print(json.dumps(data, indent=4))
        assert data["title"] == self.payload.__dict__["title"]
        product_id = data["id"]

    @pytest.mark.run(order=9)
    @pytest.mark.dependency(depends=["add_product"])
    def test_update_product(self, product_client):
        product_id = self.config.get_property("productId")
        response = product_client.update_product(product_id, self.payload)
        assert response.status_code == 200
        data = response.json()
        # print(json.dumps(data, indent=4))
        assert data["title"] == self.payload.title

    @pytest.mark.run(order=10)
    @pytest.mark.dependency(depends=["add_product"])
    def test_delete_product(self, product_client):
        product_id = self.config.get_property("productId")
        response = product_client.delete_product(product_id)
        assert response.status_code == 200
        data = response.json()
        # print(json.dumps(data, indent=4))