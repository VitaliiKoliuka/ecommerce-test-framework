import pytest

from utils.config import VALID_CREDENTIALS
from utils.config import INVALID_LOGIN_TEST_DATA
from utils.validation import AppValidation

def test_successfully_login(setup_login_page, validation):
    login_page = setup_login_page
    login_page.perform_login(VALID_CREDENTIALS["Username"],VALID_CREDENTIALS["Password"])
    validation.validate_logged_in()




@pytest.mark.parametrize("data", INVALID_LOGIN_TEST_DATA)
def test_invalid_login_and_verify_error_message(setup_login_page, validation, data):
    login_page = setup_login_page
    login_page.perform_login(data["username"], data["password"])
    validation.validate_failed_login(data["error"])