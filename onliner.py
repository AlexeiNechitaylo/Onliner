from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import pytest

class Test_onliner(unittest.TestCase):
	def setUp(self):
		self.wd = webdriver.Chrome()


	def open_page(self, wd):
		wd.get("https://www.onliner.by/")


	def login(self, wd):
		self.open_page(wd)
		wd.maximize_window()
		wd.find_element_by_css_selector("div.auth-bar div div.auth-bar").click() #click entry button
		wd.find_element_by_xpath("//input[@placeholder='Ник или e-mail']").clear()
		wd.find_element_by_xpath("//input[@placeholder='Ник или e-mail']").send_keys("ravlikgicel@gmail.com")
		wd.find_element_by_xpath("//input[@placeholder='Пароль']").clear()
		wd.find_element_by_xpath("//input[@placeholder='Пароль']").send_keys("6qwe1qwe")
		wd.find_element_by_css_selector("div.auth-form button.auth-button").click()
		

	def find_goods_and_add_to_cart(self, wd):
		wd.find_element_by_css_selector("input.fast-search__input").clear()
		wd.find_element_by_css_selector("input.fast-search__input").send_keys("духовая печь")
		
		
		
	def tearDown(self):
		self.wd.quit()
'''
	def click_cart(self, wd):
		cart_icon = WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#cart-desktop a.b-top-profile__cart")))
		cart_icon.click()


	def click_onliner_header(self, wd):
		wd.find_element_by_css_selector("header.g-top div div div a img").click()


	def logout(self, wd):
		log_out_step_1 = WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#userbar.b-top-profile div.b-top-profile__image")))
		log_out_step_1.click()
		log_out_step_2 = wd.find_element_by_css_selector("div.b-top-profile__logout a").click()


	def test_onliner(self):
		wd = self.wd
		self.login(wd)
		self.find_goods(wd)
		self.add_to_cart(wd)
		self.click_onliner_header(wd)
		self.logout(wd)
'''




if __name__== '__main__':
	unittest.main()

'''
email: ravlikgicel@gmail.com
passw: 6qwe1qwe

driver.quit()

Unittest - тестовый фреймворк
Обязательное условие - тестовый класс должен быть наследником класса unittest.TestCase и
тестовые методы должны быть размещены внутри таких классов.

setUp - метод инициализации или подготовки, которая выполняется перед тестовым методом (запускаем драйвер) 
tearDown - метод, которые выполняется после тестового метода

'''






