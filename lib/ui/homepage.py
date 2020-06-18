from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class home_page:
    def __init__(self,driver):
        self.driver=driver
    def get_logoutbutton(self):
        try:
            return self.driver.find_element_by_id("logoutLink")
        except:
            return None
    def getusersbutton(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='Users']")
        except:
            return None
    def wait_homepage(self):
        wait=WebDriverWait(driver=self.driver,timeout=30)
        wait.until(expected_conditions.visibility_of(self.get_logoutbutton()))
        wait.until(expected_conditions.visibility_of(self.getusersbutton()))