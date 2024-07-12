import pytest
from demoblaze import Demoblaze
from selenium.webdriver.common.by import By


@pytest.fixture
def demoblaze():
    db = Demoblaze()
    yield db
    db.close()


def test_navigate_to_product_page(demoblaze):
    demoblaze.navigate_to_category("Laptops")
    demoblaze.select_product("Sony vaio i5")
    product_title = demoblaze.driver.find_element(By.XPATH, "//h2[contains(text(), 'Sony vaio i5')]")
    assert product_title is not None
