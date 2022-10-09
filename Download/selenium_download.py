import lista

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class Selenium_Download():
    def __init__(self, driver, exe, element):
        options = Options()
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", "./executaveis")

        self.browser = webdriver.Firefox(
            executable_path=driver, options=options)
        self.browser.minimize_window()
        self.browser.get(exe)
        self.browser.find_element(
            by="xpath", value=element).click()
    