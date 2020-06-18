import unittest
import json
from lib.ui.homepage import home_page
from lib.ui.login_page import loginpage
from lib.utils import create_driver
from lib.ui.userspage import user_page
class testadduser12345(unittest.TestCase):
    def setUp(self):
        self.driver=create_driver.get_driver_instance()
        self.login=loginpage(self.driver)
        self.home=home_page(self.driver)
        self.user=user_page(self.driver)
    def tearDown(self):
        self.driver.close()
    def testadduser_success(self):
        user_data=json.load(open("test/reggression/users/users.json"))
        login_data=json.load(open("test/reggression/login/login.json"))
        self.login.waitfor_login()
        self.login.getusername_txtbox().send_keys(login_data['TC12345']['username'])
        self.login.getpaswd_txtbox().send_keys(login_data['TC12345']['password'])
        self.login.getlogin_button().click()
        self.home.wait_homepage()
        self.home.getusersbutton().click()
        self.user.getnewuserbutton().click()
        self.user.wait_userpage()
        self.user.getnewuser_name().send_keys(user_data['TC12']['firstname'])
        self.user.getnewuserlast_name().send_keys(user_data['TC12']['lastname'])
        self.user.getnewuser_email().send_keys(user_data['TC12']['useremail'])
        self.user.get_departmentdropdown().click()
        self.user.get_department_value().click()
        self.user.get_hiredateconatiner().click()
        self.user.get_hiredate().click
        self.user.get_savebutton().click()
        te=self.user.get_savesuccess()
        text=te.text
        assert text=="The invitation has been sent to the user's email address: j@gmail.com"



