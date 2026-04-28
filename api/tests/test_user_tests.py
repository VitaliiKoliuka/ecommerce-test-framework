import requests
import pytest
import json
# from routes.Routes import Routes
from utils.data_generator import Payload
from dataclasses import asdict

class TestUserAPI:
    @pytest.fixture(autouse=True)
    def init_class_vars(self,setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]
        self.payload = Payload()

    @pytest.mark.sanity
    @pytest.mark.run(order=1)
    def test_get_all_users(self, user_client):
        response = user_client.get_all_users()
        assert response.status_code==200
        data = response.json()
        # print(json.dumps(data,indent=4))
        assert len(data)>0

    @pytest.mark.sanity
    @pytest.mark.run(order=2)
    def test_get_user_by_id(self, user_client):
        user_id = self.config.get_property("userId")
        response = user_client.get_user_by_id(user_id)
        assert response.status_code == 200
        data = response.json()
        # print(json.dumps(data, indent=4))

    @pytest.mark.sanity
    @pytest.mark.run(order=3)
    def test_get_users_with_limit(self, user_client):
        limit = self.config.get_property("limit")
        response = user_client.get_users_with_limit(limit)
        assert response.status_code == 200
        data = response.json()
        # print(json.dumps(data, indent=4))
        assert len(data) == int(limit)

    @pytest.mark.sanity
    @pytest.mark.run(order=4)
    def test_get_users_sorted_desc(self, user_client):
        response = user_client.get_users_sorted_desc()
        assert response.status_code == 200
        data = response.json()
        users = data["users"]
        # print(json.dumps(data, indent=4))
        ids = [user["firstName"] for user in users]
        assert ids == sorted(ids, reverse=True)

    @pytest.mark.sanity
    @pytest.mark.run(order=5)
    def test_get_users_sorted_asc(self, user_client):
        response = user_client.get_users_sorted_asc()
        assert response.status_code == 200
        data = response.json()
        users = data["users"]
        # print(json.dumps(data, indent=4))
        ids = [user["firstName"] for user in users]
        assert ids == sorted(ids)

    @pytest.mark.smoke
    @pytest.mark.run(order=6)
    @pytest.mark.dependency(name="add_user")
    def test_create_user(self, user_client):
        user_payload = self.payload.user_payload()
        response = user_client.create_user(user_payload)
        assert response.status_code == 201
        data = response.json()
        # print(json.dumps(data, indent=4))
        assert "id" in data
        print("Generated UserID:", data["id"])

    @pytest.mark.regression
    @pytest.mark.run(order=7)
    @pytest.mark.dependency(depends=["add_user"])
    def test_update_user(self, user_client):
        user_id = self.config.get_property("userId")
        updated_user = self.payload.user_payload()
        response = user_client.update_user(user_id, updated_user)
        assert response.status_code == 200
        data = response.json()
        # print(json.dumps(data, indent=4))
        assert data["username"] == updated_user.username

    @pytest.mark.regression
    @pytest.mark.run(order=8)
    @pytest.mark.dependency(depends=["add_user"])
    def test_delete_user(self, user_client):
        user_id = self.config.get_property("userId")
        response = user_client.delete_user(user_id)
        assert response.status_code == 200
        data = response.json()
        # print(json.dumps(data, indent=4))

    def test_login(self, auth_client):
        payload = self.payload.login_payload(self.config)
        response = auth_client.login(payload)
        # print(response.status_code)
        # print(response.text)
        # print(payload)
        # print(response.url)
        assert response.status_code == 200
        data = response.json()
        expected_username = self.config.get_property("username")
        assert "accessToken" in data
        assert "refreshToken" in data
        assert data["username"] == expected_username


    def test_get_current_user(self, auth_client, auth_token):
        response = auth_client.get_current_user(auth_token)
        assert response.status_code == 200

        data = response.json()
        assert "id" in data
        assert "email" in data






















