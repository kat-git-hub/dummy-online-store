import time
from config import Config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class Demoblaze:
    def __init__(self):
        service = Service(executable_path=Config.DRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(Config.IMPLICIT_WAIT)
        self.driver.get(Config.BASE_URL)

    def navigate_to_category(self, category):
        category_link = self.driver.find_element(By.XPATH, f"//a[text()='{category}']")
        category_link.click()

    def select_product(self, product_name):
        product_link = self.driver.find_element(By.XPATH, f"//a[contains(text(), '{product_name}')]")
        product_link.click()

    def add_to_cart(self):
        add_to_cart_button = self.driver.find_element(By.XPATH, "//a[text()='Add to cart']")
        add_to_cart_button.click()
        time.sleep(2)  # Wait for alert
        self.driver.switch_to.alert.accept()

    def go_to_cart(self):
        cart_link = self.driver.find_element(By.XPATH, "//a[text()='Cart']")
        cart_link.click()

    def place_order(self, name, country, city, card, month, year):
        place_order_button = self.driver.find_element(By.XPATH, "//button[text()='Place Order']")
        place_order_button.click()

        self.driver.find_element(By.ID, "name").send_keys(name)
        self.driver.find_element(By.ID, "country").send_keys(country)
        self.driver.find_element(By.ID, "city").send_keys(city)
        self.driver.find_element(By.ID, "card").send_keys(card)
        self.driver.find_element(By.ID, "month").send_keys(month)
        self.driver.find_element(By.ID, "year").send_keys(year)

        purchase_button = self.driver.find_element(By.XPATH, "//button[text()='Purchase']")
        purchase_button.click()

    def close(self):
        self.driver.quit()
