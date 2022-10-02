import lista

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class Selenium_Download():
    def Download_VS(self):
        options = Options()
        options.set_preference("browser.download.dir", "./executaveis")
        
        self.browser = webdriver.Firefox(executable_path='driver\geckodriver.exe', options=options)
        self.browser.minimize_window()
        self.browser.get(lista.download_visual_studio[0])
        self.browser.find_element(
            by="xpath", value="/html/body/div[3]/main/div/div/div/div/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div[1]/div/div[3]/div/div/a/span").click()
        
    def Download_Postman(self):
        options = Options()
        options.set_preference("browser.download.dir", "./executaveis")

        self.browser = webdriver.Firefox(
            executable_path='driver\geckodriver.exe', options=options)
        self.browser.minimize_window()
        self.browser.get(lista.download_postman[0])
        self.browser.find_element(
            by="xpath", value="//*[@id=\"download-the-app-windows-64\"]").click()
        
    def Download_Vscode(self):
        options = Options()
        options.set_preference("browser.download.dir", "./executaveis")

        self.browser = webdriver.Firefox(
            executable_path='driver\geckodriver.exe', options=options)
        self.browser.minimize_window()
        self.browser.get(lista.download_visual_studio_code[0])
        self.browser.find_element(
            by="xpath", value="//*[@id=\"download-alt-win\"]").click()
        
    def Download_Kanban_Tasker(self):
        options = Options()
        options.set_preference("browser.download.dir", "./executaveis")

        self.browser = webdriver.Firefox(
            executable_path='driver\geckodriver.exe', options=options)
        self.browser.minimize_window()
        self.browser.get(lista.download_kanban_tasker[0])
        self.browser.find_element(
            by="xpath", value="/html/body/div/div[3]/div/div/div[1]/div[1]/div[2]/button/span/div/font").click()

    