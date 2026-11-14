from Pages.login_page import LoginPage
from Utilities.common import Common

def test_valid_login(setup):
    driver=setup

    Common.login(driver,'standard_user','secret_sauce')

    assert 'inventory' in driver.current_url
