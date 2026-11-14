from selenium.webdriver.common.by import By


class LoginPage:
    username_id = 'user-name'
    password_id = 'password'
    login_btn_id = 'login-button'

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_btn_id).click()