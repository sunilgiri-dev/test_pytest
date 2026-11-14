from selenium.webdriver.common.by import By
from Pages.inventory_page import InventoryPage
from Utilities.common import Common

def test_add_and_remove_from_cart(setup):
    driver = setup
    Common.login(driver, "standard_user", "secret_sauce")
    inventory = InventoryPage(driver)

    inventory.add_to_cart()
    assert driver.find_element(By.ID, "shopping_cart_badge").text == "1"

    inventory.remove_from_cart()
    assert not driver.find_elements(By.ID, "shopping_cart_badge")