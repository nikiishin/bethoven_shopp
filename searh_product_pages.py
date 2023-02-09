import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utulite.logger import Logger


class Search_product_page(Base):
    url = 'https://www.bethowen.ru/'
    url_search = 'https://www.bethowen.ru/search/?q=grandorf'

        # Location

    search_line = "//*[@id='title-search-input_fixed']"
    search_line_2 = "//*[@id='no_modal_adv']"
    cat = "//*[@id='diginetika-result']/div/div[1]/div[2]/div[4]/div[2]/div[3]/label/div[1]/input"
    sorted_butten = "//*[@id='diginetika-result']/div/div[1]/div[3]/div[1]/select"
    select_prod = "//*[@id='diginetika-result']/div/div[1]/div[3]/div[1]/div/div[2]/a/img"
    word_prod = "//*[@id='bx_117848907_342620_sku_name_prop']"
    select_wigth = "//*[@id='bx_117848907_342620_prop_290_list']/li[2]/span"
    select_cart = "//*[@id='bx_117848907_342620']/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/span"
    go_cart = "//*[@id='header']/div/div[1]/div/div/div/div[3]/div[1]/div[3]/a"
    cart_word = "//*[@id='dgn__order-page-container']/h1"
    deliv_shopp = "//*[@id='t-delivery-list-btn-from_shop']"
    go_to_spicok = "//*[@id='dgn__order-page-container']/div/div[1]/div[3]/section[1]/div[3]/div/div/div[1]/div[" \
                   "2]/button[2] "
    adress_shop_search = "//*[@id='dgn__order-page-container']/div/div[1]/div[3]/section[1]/div[3]/div/div/div[" \
                         "3]/div[1]/div/input "

    select_button_shopp = "//*[@id='dgn__order-page-container']/div/div[1]/div[3]/section[1]/div[3]/div/div/div[" \
                          "3]/div[2]/div/div[2]/div[2]/button "
    name = "//*[@id='dgn__order-page-container']/div/div[1]/div[3]/section[3]/div[2]/div[4]/input"
    sername = "//*[@id='dgn__order-page-container']/div/div[1]/div[3]/section[3]/div[2]/div[3]/input"
    mail = "//*[@id='dgn__order-page-container']/div/div[1]/div[3]/section[3]/div[2]/div[2]/input"
    number_phone = "//*[@id='dgn__order-page-container']/div/div[1]/div[3]/section[3]/div[2]/div[1]/input"
    def get_search_line(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_line)))

    def get_search_line_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_line_2)))
    def get_cat(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cat)))
    def get_select_prod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_prod)))
    def get_word_prod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_prod)))

    def get_select_wigth(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_wigth)))
    def get_select_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cart)))

    def get_go_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_cart)))

    def get_word_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_word)))

    def get_deliv_shopp(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.deliv_shopp)))
    def get_go_to_spicok(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_spicok)))

    def get_adress_shop_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self. adress_shop_search)))

    def get_select_button_shopp(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_button_shopp)))

    def get_number_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_phone)))
    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail)))
    def get_sername(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sername)))
    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))



    def search_product_grandorff(self):
        with allure.step('search_product_grandorff'):


            Logger.add_start_step(method='search_product_grandorff')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_search_line().click()
            print('Переходим в строку поиска')
            self.get_search_line_2().send_keys("grandorff")
            print('Ищем корм Grandorff')
            time.sleep(3)
            self.get_search_line_2().send_keys(Keys.ENTER)
            self.get_cat().click()
            print('Выбираем для кошек')
            self.get_current_url()
            self.get_select_prod().click()

            self.assert_word(self.get_word_prod(), 'Корм для кошек GRANDORF для живущих в помещении, ягненок с рисом сух.')
            self.get_select_wigth().click()
            print('Выбираем вес 2кг')
            self.get_select_cart().click()
            self.get_go_cart().click()
            print("Переходим в корзину")
            self.assert_word(self.get_word_cart(), 'Ваша корзина 1 шт.')
            self.get_deliv_shopp().click()
            print('Выбиоаем способ доставки')
            self.get_go_to_spicok().click()
            self.get_adress_shop_search().send_keys('Братиславская')
            self.get_select_button_shopp().click()
            self.get_number_phone().send_keys('+07566965556')
            self.get_mail().send_keys('qwert@gmail.com')
            self.get_sername().send_keys('Natan')
            self.get_name().send_keys('Kaban')
            Logger.add_end_step(url=self.driver.current_url, method='search_product_grandorff')










