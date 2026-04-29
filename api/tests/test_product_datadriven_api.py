import requests
import os
import pytest
import json
from api.routes import Routes
from api.schemas.product_schema import Product
from utils.helpers import DataProvider
from dataclasses import asdict
from pathlib import Path


#Get File Path
path = Path(__file__).resolve().parents[2] / "data" / "products.json"

class TestProductAPI:
    @pytest.fixture(autouse=True)
    def init_class_vars(self,setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]

    @pytest.mark.regression
    @pytest.mark.parametrize('order_data',DataProvider.read_json_data(path))
    def test_add_new_delete_product(self,order_data, product_client):
        product_data = order_data[0]

        #Extract fields
        title = product_data["title"]
        price = float(product_data["price"])
        category = product_data["category"]
        description = product_data["description"]
        image = product_data["image"]

        payload = Product(title, price, description, image, category)
        # payload_dict = asdict(payload)

        # Adding Product
        response = product_client.create_product(payload)
        assert response.status_code in [201, 404]
        data = response.json()
        # print(json.dumps(data, indent=4))

        #Validations
        assert data["title"] == payload.title
        assert float(data["price"]) == payload.price
        assert data["category"] == payload.category
        product_id = data["id"]


        #Delete Product
        # endpoint = self.base_url+Routes.DELETE_PRODUCT.format(id=product_id )
        response = product_client.delete_product(product_id)
        assert response.status_code in [200, 404]
        data = response.json()
        # print(json.dumps(data, indent=4))
        if response.status_code == 200:
            assert data["id"] == product_id
        elif response.status_code == 404:
            assert "message" in data















