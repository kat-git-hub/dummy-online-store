from config import Config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class Demoblaze:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Remote(
            command_executor=Config.SELENIUM_HUB_URL,
            options=chrome_options
        )
        self.driver.implicitly_wait(Config.IMPLICIT_WAIT)
        self.driver.get(Config.BASE_URL)

    def navigate_to_category(self, category_name):
        category_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, category_name))
        )
        category_link.click()

    def select_product(self, product_name):
        while True:
            try:
                product_link = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, product_name))
                )
                product_link.click()
                break
            except StaleElementReferenceException:
                continue

    def add_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Add to cart')]"))
        )
        add_to_cart_button.click()

    def go_to_cart(self):
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "Cart"))
        )
        cart_link.click()

    def place_order(self, name, country, city, card, month, year):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        ).send_keys(name)
        self.driver.find_element(By.ID, "country").send_keys(country)
        self.driver.find_element(By.ID, "city").send_keys(city)
        self.driver.find_element(By.ID, "card").send_keys(card)
        self.driver.find_element(By.ID, "month").send_keys(month)
        self.driver.find_element(By.ID, "year").send_keys(year)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Purchase')]").click()

    def close(self):
        self.driver.quit()
