from Pages.login_page import LoginPage

class Common:
    @staticmethod
    def login(driver,username,password):
        login = LoginPage(driver)

        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
