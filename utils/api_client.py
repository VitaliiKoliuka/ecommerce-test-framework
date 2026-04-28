import requests
from utils.logger import get_logger
from config.settings import BASE_URL

logger = get_logger(__name__)

class APIClient:
    BASE_URL = BASE_URL

    def get(self, endpoint, **kwargs):
        url = self.BASE_URL + endpoint
        response = requests.get(url, **kwargs)
        self._log(response)
        return response

    def post(self, endpoint, **kwargs):
        url = self.BASE_URL + endpoint
        response = requests.post(url, **kwargs)
        self._log(response)
        return response

    def put(self, endpoint, **kwargs):
        url = self.BASE_URL + endpoint
        response = requests.put(url, **kwargs)
        self._log(response)
        return response

    def _log(self, response):
        req = response.request
        logger.info(f"{req.method} {req.url}")
        logger.info(f"Status: {response.status_code}")