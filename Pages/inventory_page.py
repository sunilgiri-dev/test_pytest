from selenium.webdriver.common.by import By


class InventoryPage:
    add_to_cart_button = "add-to-cart-sauce-labs-backpack"
    remove_button = "remove-sauce-labs-backpack"
    cart_link = "shopping_cart_link"

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.ID, self.add_to_cart_button).click()

    def remove_from_cart(self):
        self.driver.find_element(By.ID, self.remove_button).click()

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, self.cart_link).click()

