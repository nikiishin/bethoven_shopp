from selenium import webdriver
import pytest
import allure
from pages.searh_product_pages import Search_product_page

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

@allure.description('test_buy_product_1')
def test_buy_product_1(set_up):
    # driver_service = Service(executable_path='C:\\Users\\Nikita\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(executable_path='C:\\Users\\Nikita\\PycharmProjects\\resource\\chromedriver.exe', options=options)
    # driver = webdriver.Chrome(service=driver_service)
    print("Start 1 ")
    s_p = Search_product_page(driver)
    s_p.search_product_grandorff()
