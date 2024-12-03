import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class BaseClass(unittest.TestCase):

    def setUp(self) -> None:
        service = Service(executable_path='./chromedriver.exe')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--headless=new')

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
