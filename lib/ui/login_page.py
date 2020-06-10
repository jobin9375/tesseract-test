from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class loginpage:
    def __init__(self,driver):
        self.driver=driver
    def getusername_txtbox(self):
        try:
            un=self.driver.find_element_by_id("username")
            return un
        except:
            return None
    def getpaswd_txtbox(self):
        try:
            return self.driver.find_element_by_name("pwd")
        except:
            return None
    def getlogin_button(self):
        try:
            return self.driver.find_element_by_id("loginButtonContainer")
        except:
            return None
    def getlogin_error(self):
        try:
            return self.driver.find_element_by_xpath("//span[text()='Username or Password is invalid. Please try again.']")
        except:
            return None
    def waitfor_login(self):
        wait=WebDriverWait(driver=self.driver,timeout=10)
        wait.until(expected_conditions.visibility_of(self.getusername_txtbox()))
        wait.until(expected_conditions.visibility_of(self.getpaswd_txtbox()))
        wait.until(expected_conditions.visibility_of(self.getlogin_button()))