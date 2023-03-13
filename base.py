from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:
    def __init__(self, url) -> None:
        self.options = Options()
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=self.options)

        self.url = url

    def get_page(self):
        self.driver.get(self.url)

    def get_element(self, value):
        return self.driver.find_element(By.XPATH, value)

    def click_on_element(self,  value):
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, value))))

    def close_context(self):
        self.driver.close()




