from utils.api_client import APIClient
from api.routes import Routes

class AuthClient(APIClient):

    def login(self, payload):
        return self.post(Routes.CREATE_LOGIN, json=payload)

    def get_current_user(self, token):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        return self.get(Routes.GET_CURRENT_USER, headers=headers)