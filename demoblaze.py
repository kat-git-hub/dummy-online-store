from config import Config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class Demoblaze:
    def __init__(self, selenium_hub_url=None, base_url=None, implicit_wait=None, chrome_options=None):
        self.driver = self._setup_driver(selenium_hub_url, chrome_options)
        self.driver.implicitly_wait(implicit_wait or Config.IMPLICIT_WAIT)
        self.driver.get(base_url or Config.BASE_URL)

    def _setup_driver(self, selenium_hub_url, chrome_options):
        if chrome_options is None:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')

        driver = webdriver.Remote(
            command_executor=selenium_hub_url or Config.SELENIUM_HUB_URL,
            options=chrome_options
        )
        return driver

    def navigate_to_category(self, category_name):
        category_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, category_name))
        )
        category_link.click()

    def select_product(self, product_name):
        while True:
            try:
                product_link = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, product_name))
                )
                product_link.click()
                break
            except StaleElementReferenceException:
                continue

    def add_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Add to cart')]"))
        )
        add_to_cart_button.click()

    def go_to_cart(self):
        cart_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "cartur"))
        )
        cart_link.click()

    def place_order(self, name, country, city, card, month, year):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]"))
        ).click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "name"))
        ).send_keys(name)
        self.driver.find_element(By.ID, "country").send_keys(country)
        self.driver.find_element(By.ID, "city").send_keys(city)
        self.driver.find_element(By.ID, "card").send_keys(card)
        self.driver.find_element(By.ID, "month").send_keys(month)
        self.driver.find_element(By.ID, "year").send_keys(year)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Purchase')]").click()

    def close(self):
        if self.driver:
            try:
                self.driver.quit()
            except Exception:
                pass
