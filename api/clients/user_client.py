from utils.api_client import APIClient
from api.routes import Routes
from dataclasses import asdict

class UserClient(APIClient):

    def get_all_users(self):
        return self.get(Routes.GET_ALL_USERS)

    def get_user_by_id(self, user_id):
        endpoint = Routes.GET_USER_BY_ID.format(id=user_id)
        return self.get(endpoint)

    def get_users_with_limit(self, limit):
        endpoint = Routes.GET_USERS_WITH_LIMIT.format(limit=limit)
        return self.get(endpoint)

    def get_users_sorted_desc(self):
        endpoint = Routes.GET_USERS_SORTED.format(order="desc")
        return self.get(endpoint)

    def get_users_sorted_asc(self):
        endpoint = Routes.GET_USERS_SORTED.format(order="asc")
        return self.get(endpoint)

    def create_user(self, payload):
        return self.post(Routes.CREATE_USER, json=asdict(payload))

    def update_user(self, user_id, payload):
        return self.put(Routes.UPDATE_USER.format(id=user_id), json=asdict(payload))

    def delete_user(self, user_id):
        endpoint = Routes.DELETE_USER.format(id=user_id)
        return self.get(endpoint)