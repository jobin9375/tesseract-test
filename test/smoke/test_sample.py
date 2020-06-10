import unittest
from lib.ui.login_page import loginpage
from lib.utils import create_driver
class testtsample(unittest.TestCase):
    def setUp(self):
        self.driver=create_driver.get_driver_instance()
        self.login=loginpage(self.driver)
    def tearDown(self):
        self.driver.close()
    def test_invlalidlogin(self):
        self.login.waitfor_login()
        self.login.getusername_txtbox().send_keys("invalid")
        self.login.getpaswd_txtbox().send_keys("invalid")
        self.login.getlogin_button().click()
        actual_error=self.login.getlogin_error().text
        expected_error="Username or Password is invalid. Please try again."
        assert actual_error==expected_error,"not matching"