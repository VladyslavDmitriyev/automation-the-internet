from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SecureZone(BasePage):
    _url = "https://the-internet.herokuapp.com/secure"
    _success_message = (By.ID, "flash")
    _logout_button = (By.CLASS_NAME, "icon-signout")

    def __init__(self, driver):
        self.driver = driver

    def visit_secure_zone(self):
        self._visit(self._url)

    def is_secure_zone_page(self):
        assert self.driver.current_url == self._url

    def is_success_message(self):
        return self._is_displayed(self._success_message)
    
    def success_message_content(self):
        return self._find(self._success_message).text
    
    def is_logout_button(self):
        return self._is_displayed(self._logout_button)
    
    def perform_logout(self):
        self._click(self._logout_button)