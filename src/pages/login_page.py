from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from src.tests import config


class LoginPage(BasePage):
    _url = "/login"
    _form_username = (By.ID, "username")
    _form_password = (By.ID, "password")
    _button_login = (By.CLASS_NAME, "fa-sign-in")
    _button_logout = (By.NAME, "Logout")
    _success_message = (By.ID, "flash")
    _all_login_form_fields = (_form_username, _form_password)

    def __init__(self, driver):
        super().__init__(driver)

    def visit_login_page(self):
        self._visit(self._url)
    
    def is_login_page(self):
        return self.driver.current_url == config.baseurl + self._url

    def perform_login(self, form_inputs):
        fields_len, inputs_len = len(self._all_login_form_fields), len(form_inputs)
        assert fields_len == inputs_len
        
        for i in range(fields_len):
            self._type(self._all_login_form_fields[i], form_inputs[i])

        self._click(self._button_login)
    
    def is_success_message(self):
        return self._is_displayed(self._success_message)
    
    def success_message_content(self):
        return self._find(self._success_message).text
