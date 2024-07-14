import time
import pytest
from selenium.webdriver.common.by import By
from demoblaze import Demoblaze


@pytest.fixture
def demoblaze():
    db = Demoblaze()
    yield db
    db.close()


def test_navigate_to_category(demoblaze):
    demoblaze.navigate_to_category("Laptops")
    time.sleep(2)
    category_elements = demoblaze.driver.find_elements(By.CLASS_NAME, "card-title")
    assert len(category_elements) > 0


def test_select_product(demoblaze):
    demoblaze.navigate_to_category("Laptops")
    demoblaze.select_product("Dell i7 8gb")
    time.sleep(2)
    product_title = demoblaze.driver.find_element(By.XPATH, "//h2[contains(text(), 'Dell i7 8gb')]")
    assert product_title is not None


def test_add_product_to_cart(demoblaze):
    demoblaze.navigate_to_category("Phones")
    demoblaze.select_product("Samsung galaxy s6")
    demoblaze.add_to_cart()
    demoblaze.go_to_cart()
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
    confirmation = demoblaze.driver.find_element(By.XPATH, "//h2[contains(text(), 'Thank you for your purchase!')]")
    assert confirmation is not None


def test_go_to_cart(demoblaze):
    demoblaze.navigate_to_category("Laptops")
    demoblaze.select_product("MacBook air")
    demoblaze.add_to_cart()
    demoblaze.go_to_cart()
    cart_header = demoblaze.driver.find_element(By.XPATH, "//h2[contains(text(), 'Products')]")
    assert cart_header is not None


def test_close_browser(demoblaze):
    demoblaze.close()
    try:
        demoblaze.driver.title
    except Exception:
        assert True
