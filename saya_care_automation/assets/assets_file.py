from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Assets:
    def __init__(self):
        option = Options()
        option.add_experimental_option("detach", True)
        self.browser = wd.Chrome(options=option)
        self.action = wd.ActionChains(self.browser, duration=2000)

    def url(self):
        self.browser.get("https://saya.net.in")

    def explict_wait(self, time_out, xpath, attribute_x_path):
        WebDriverWait(self.browser, time_out).until(EC.visibility_of_element_located((xpath, attribute_x_path)))

    def single_element_find(self, xpath, attribute_x_path):
        element = self.browser.find_element(xpath, attribute_x_path)
        return element

    def multiple_element_find(self, xpath, attribute_x_path):
        multiple_elements = self.browser.find_elements(xpath, attribute_x_path)
        return multiple_elements

    def action_chain(self, xpath, attribute_x_path):
        self.action.move_to_element(
            self.browser.find_element(xpath, attribute_x_path)).click().perform()
