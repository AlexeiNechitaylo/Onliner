from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()


    def open_page(self):
        wd = self.wd
        wd.get("https://www.onliner.by/")


    def login(self, user_data):
        wd = self.wd
        self.open_page()
        wd.maximize_window()
        wd.find_element_by_css_selector("div.auth-bar div div.auth-bar").click()  # click entry button
        wd.find_element_by_xpath("//input[@placeholder='Ник или e-mail']").clear()
        wd.find_element_by_xpath("//input[@placeholder='Ник или e-mail']").send_keys(user_data.email)
        wd.find_element_by_xpath("//input[@placeholder='Пароль']").clear()
        wd.find_element_by_xpath("//input[@placeholder='Пароль']").send_keys(user_data.password)
        wd.find_element_by_css_selector("div.auth-form button.auth-button").click()


    def click_cart(self):
        wd = self.wd
        cart_icon = WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#cart-desktop a.b-top-profile__cart")))
        cart_icon.click()


    def click_onliner_header(self):
        wd = self.wd
        wd.find_element_by_css_selector("header.g-top div div div a img").click()


    def logout(self):
        wd = self.wd
        log_out_step_1 = WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#userbar.b-top-profile div.b-top-profile__image")))
        log_out_step_1.click()
        wd.find_element_by_css_selector("div.b-top-profile__logout a").click()


    def destroy(self):
        self.wd.quit()