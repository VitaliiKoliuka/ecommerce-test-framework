import pytest
import requests
import allure
import json
from api.routes import Routes
from config.settings import ReadConfig
from api.clients.product_client import ProductClient
from api.clients.cart_client import CartClient
from api.clients.user_client import UserClient
from api.clients.auth_client import AuthClient
from utils.logger import get_logger
from utils.data_generator import Payload


@pytest.fixture
def product_client():
    return ProductClient()

@pytest.fixture
def cart_client():
    return CartClient()

@pytest.fixture
def user_client():
    return UserClient()

@pytest.fixture(scope="session")
def config():
    return ReadConfig()

@pytest.fixture(scope="session")
def payload():
    return Payload()

@pytest.fixture(scope="session")
def auth_client():
    return AuthClient()

@pytest.fixture(scope="session")
def auth_token(auth_client, payload, config):
    login_payload = payload.login_payload(config)
    response = auth_client.login(login_payload)

    assert response.status_code == 200
    return response.json()["accessToken"]

logger = get_logger(__name__)
def log_request_response(response):
    req = response.request

    request_info = {
        "method": req.method,
        "url": req.url,
        "headers": dict(req.headers),
        "body": req.body.decode() if isinstance(req.body, bytes) else req.body
    }

    try:
        response_body = response.json()
    except Exception:
        response_body = response.text

    response_info = {
        "status_code": response.status_code,
        "headers": dict(response.headers),
        "body": response_body
    }

    allure.attach(
        json.dumps(request_info, indent=2),
        name="Request",
        attachment_type=allure.attachment_type.JSON
    )

    allure.attach(
        json.dumps(response_info, indent=2),
        name="Response",
        attachment_type=allure.attachment_type.JSON
    )

    logger.info(f"REQUEST: {req.method} {req.url}")
    logger.info(f"Request Headers: {req.headers}")

    if req.body:
        logger.info(f"Request Body: {req.body}")

    logger.info(f"RESPONSE Status: {response.status_code}")
    logger.info(f"Response Headers: {response.headers}")

    try:
        logger.info(f"Response Body: {response.json()}")
    except Exception:
        logger.info(f"Response Body: {response.text}")


@pytest.fixture(scope="session", autouse=True)
def setup():
    original_request = requests.Session.request

    def custom_request(self, method, url, **kwargs):
        response = original_request(self, method, url, **kwargs)
        log_request_response(response)
        return response

    requests.Session.request = custom_request

    yield {
        "base_url": Routes.BASE_URL,
        "config_reader": ReadConfig
    }

