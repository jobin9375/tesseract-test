from argparse import ArgumentParser
from selenium.webdriver import Chrome,Firefox
def get_driver_instance():
    parser=ArgumentParser()
    parser.add_argument("--browser",default="Firefox")
    parser.add_argument("--url",default="Test")
    parser.add_argument("--env",default="windows")
    options,arg=parser.parse_known_args()
    browser_type=options.browser.lower()
    url_info=options.url.lower()
    env_info=options.env.lower()
    if browser_type=="chrome":
        driver=Chrome("./Browser_servers/chromedriver.exe")
    elif browser_type=="firefox":
        driver=Firefox(executable_path="./Browser_servers/geckodriver.exe")
    else:
        print("invalid browser option")
    driver.maximize_window()
    driver.implicitly_wait(30)
    if url_info=="test":
        driver.get("https://demo.actitime.com/login.do")
    elif url_info=="prod":
        driver.get("https://demo.actitime.com/login.do")
    else:
        driver.get("https://www.google.com")
    return driver

