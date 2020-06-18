from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class user_page:
    def __init__(self,driver):
        self.driver=driver
    def getnewuserbutton(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='New User']")
        except:
            return None
    def getnewuser_name(self):
        try:
            return self.driver.find_element_by_id("createUserPanel_firstNameField")
        except:
            return None
    def getnewuserlast_name(self):
        try:
            return self.driver.find_element_by_id("createUserPanel_lastNameField")
        except:
            return None
    def getnewuser_email(self):
            try:
                return self.driver.find_element_by_id("createUserPanel_emailField")
            except:
                return None
    def get_departmentdropdown(self):
            try:
                return self.driver.find_element_by_xpath("//div/div/div[@class='simpleListMenuButton components_userGroupSelectorMenu emptyList notEmpty']")
            except:
                return None
    def get_department_value(self):
            try:
                return self.driver.find_element_by_xpath("//div/div/div[text()='Production']")
            except:
                return None
    def get_hiredateconatiner(self):
            try:
                return self.driver.find_element_by_id("createUserPanel_hireDatePlaceholder")
            except:
                return None
    def get_hiredate(self):
            try:
                return self.driver.find_element_by_xpath("//span[text()='8']")
            except:
                return None
    def get_savebutton(self):
            try:
                return self.driver.find_element_by_xpath("//div[text()='Save & Send Invitation']")
            except:
                return None
    def get_savesuccess(self):
            try:
                return self.driver.find_element_by_xpath("//div[contains(text(),'The invitation has been sent to the')]")
            except:
                return None
    def wait_userpage(self):
        wait=WebDriverWait(driver=self.driver,timeout=30)
        wait.until(expected_conditions.visibility_of(self.getnewuser_name()))
        wait.until(expected_conditions.visibility_of(self.getnewuserlast_name()))
        wait.until(expected_conditions.visibility_of(self.getnewuser_email()))
        wait.until(expected_conditions.visibility_of(self.get_departmentdropdown()))
        wait.until(expected_conditions.visibility_of(self.get_hiredateconatiner()))
        wait.until(expected_conditions.visibility_of(self.get_savebutton()))
