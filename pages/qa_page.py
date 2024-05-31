from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

shortTimeOut = 4


class QAPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://rahulshettyacademy.com/AutomationPractice/')
        # point 2
        self.inputXpath = self.driver.find_element(By.XPATH, '//input[@id="autocomplete"]')
        self.dropdownXpath = '//ul[@id="ui-id-1"]/li[contains(.,"%s")]'
        # point 3
        self.dropDownExample = '//select[@id="dropdown-class-example"]'
        self.optionsFromDropdown = '//select[@id="dropdown-class-example"]//option[%s]'
        self.bodyXpath = '//body/div[1]'
        self.optionsValue = '//option[text()="Option%s"]'
        # point 4
        self.openWindow = '//button[@id="openwindow"]'
        self.textNewWindow = '//*[contains(text(), "%s")]'
        # point 5
        self.openTab = '#opentab'
        self.allCoursesButton = '//a[contains(text(),"Access all our Courses")]'
        # point 6
        self.switch_to_alert_input = '//input[@id="name"]'
        self.switch_to_alert_button = '//input[@id="alertbtn"]'
        self.switch_to_alert_confirm_button = '//input[@id="confirmbtn"]'
        # point 7
        self.courses_table = '//table[@id="product" and @name="courses"]/tbody'
        # point 8
        self.second_table = '(//table[@id="product"])[2]/tbody'

    def search_for_country(self, query):
        self.inputXpath.send_keys(query[0:3], Keys.ENTER)
        WebDriverWait(self.driver, shortTimeOut).until(
            EC.presence_of_element_located((By.XPATH, self.dropdownXpath % str(query)))).click()

    def assert_country(self, query):
        WebDriverWait(self.driver, shortTimeOut).until(
            EC.presence_of_element_located((By.XPATH, self.dropdownXpath % str(query))))
        return True

    def select_option(self, query):
        self.driver.find_element(By.XPATH, self.dropDownExample).click()
        WebDriverWait(self.driver, shortTimeOut).until(
            EC.element_to_be_clickable((By.XPATH, self.optionsFromDropdown % str(query)))).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.bodyXpath).click()
        time.sleep(1)

    def assert_option(self, query):
        WebDriverWait(self.driver, shortTimeOut).until(
            EC.visibility_of_element_located((By.XPATH, self.optionsValue % str(query))))
        assert True

    def open_new_window(self):
        self.driver.find_element(By.XPATH, self.openWindow).click()

    def open_new_tab(self):
        self.driver.find_element(By.CSS_SELECTOR, self.openTab).click()

    def switch_window(self):
        time.sleep(2)
        newWindow = self.driver.window_handles[1]
        self.driver.switch_to.window(newWindow)
        time.sleep(2)

    def assert_text_present(self, query):
        oldWindow = self.driver.window_handles[0]
        try:
            self.driver.find_element(By.XPATH, self.textNewWindow % str(query))
            assert True
        except Exception:
            self.driver.close()
            self.driver.switch_to.window(oldWindow)
            return False

    def assert_button_visible(self, scenario_name, feature_name):
        screenshot_path = os.path.join("reports/screenshots", f"_{feature_name}_{scenario_name}.png")
        WebDriverWait(self.driver, shortTimeOut).until(
            EC.visibility_of_element_located((By.XPATH, self.allCoursesButton))).screenshot(screenshot_path)
        assert True

    def use_switch_alert(self, text):
        WebDriverWait(self.driver, shortTimeOut).until(
            EC.visibility_of_element_located((By.XPATH, self.switch_to_alert_input))).send_keys(text)

    def click_alert(self):
        self.driver.find_element(By.XPATH, self.switch_to_alert_button).click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()

    def click_confirm(self):
        self.driver.find_element(By.XPATH, self.switch_to_alert_confirm_button).click()
        time.sleep(2)

    def assert_alert(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def search_for_courses(self, value1, value2):
        table = self.driver.find_element(By.XPATH, self.courses_table)
        rows = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            td_values = [col.text for col in columns]
            if str(value1) in td_values:
                print(f"{td_values[0]} {td_values[2]}")
            if str(value2) in td_values:
                print(f"{td_values[0]} {td_values[2]}")

    def search_by_prof(self, value1, value2):
        table = self.driver.find_element(By.XPATH, self.second_table)
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            td_values = [col.text for col in columns]
            if str(value1) in td_values:
                print(f"{td_values[0]} {td_values[2]}")
            if str(value2) in td_values:
                print(f"{td_values[0]} {td_values[2]}")
