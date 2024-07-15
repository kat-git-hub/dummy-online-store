import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from demoblaze import Demoblaze

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')


@pytest.fixture(scope="module")
def demoblaze():
    db = Demoblaze(options=chrome_options)
    yield db
    db.close()


def test_navigate_to_category(demoblaze):
    demoblaze.navigate_to_category("Laptops")
    WebDriverWait(demoblaze.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "card-title"))
    )
    category_elements = demoblaze.driver.find_elements(By.CLASS_NAME, "card-title")
    assert len(category_elements) > 0


def test_select_product(demoblaze):
    demoblaze.navigate_to_category("Laptops")
    demoblaze.select_product("Dell i7 8gb")
    WebDriverWait(demoblaze.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Dell i7 8gb')]"))
    )
    product_title = demoblaze.driver.find_element(By.XPATH, "//h2[contains(text(), 'Dell i7 8gb')]")
    assert product_title is not None


def test_add_product_to_cart(demoblaze):
    demoblaze.navigate_to_category("Phones")
    demoblaze.select_product("Samsung galaxy s6")
    demoblaze.add_to_cart()
    demoblaze.go_to_cart()
    WebDriverWait(demoblaze.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody[@id='tbodyid']/tr"))
    )
    cart_items = demoblaze.driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']/tr")
    assert len(cart_items) > 0


def test_place_order(demoblaze):
    demoblaze.navigate_to_category("Monitors")
    demoblaze.select_product("Apple monitor 24")
    demoblaze.add_to_cart()
    demoblaze.go_to_cart()
    demoblaze.place_order(
        name="James Taylor",
        country="USA",
        city="Oklahoma",
        card="12345678910",
        month="01",
        year="2027"
    )
    WebDriverWait(demoblaze.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Thank you for your purchase!')]"))
    )
    confirmation = demoblaze.driver.find_element(By.XPATH, "//h2[contains(text(), 'Thank you for your purchase!')]")
    assert confirmation is not None


def test_go_to_cart(demoblaze):
    demoblaze.navigate_to_category("Laptops")
    demoblaze.select_product("MacBook air")
    demoblaze.add_to_cart()
    demoblaze.go_to_cart()
    WebDriverWait(demoblaze.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Products')]"))
    )
    cart_header = demoblaze.driver.find_element(By.XPATH, "//h2[contains(text(), 'Products')]")
    assert cart_header is not None


def test_close_browser(demoblaze):
    demoblaze.close()
    with pytest.raises(Exception):
        _ = demoblaze.driver.title
