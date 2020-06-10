import unittest
import json
from lib.ui.homepage import home_page
from lib.ui.login_page import loginpage
from lib.utils import create_driver
class testlogin12345(unittest.TestCase):
    def setUp(self):
        self.driver=create_driver.get_driver_instance()
        self.login=loginpage(self.driver)
        self.home=home_page(self.driver)
    def tearDown(self):
        self.driver.close()
    def test_loginsucces(self):
        data=json.load(open("test/reggression/login/login.json"))
        self.login.waitfor_login()
        self.login.getusername_txtbox().send_keys(data['TC12345']['username'])
        self.login.getpaswd_txtbox().send_keys(data['TC12345']['password'])
        self.login.getlogin_button().click()
        self.home.wait_homepage()
        actual_title=self.driver.title
        expected_title=data['TC12345']['home_page_title']
        assert actual_title==expected_title,"title is not matching"
        print(actual_title)
        self.home.get_logoutbutton().click()
        self.login.waitfor_login()
        actlogin_title=self.driver.title
        expelogin_title=data['TC12345']['login_title']
        assert actlogin_title==expelogin_title,"logout is failed"
        print(actlogin_title)

