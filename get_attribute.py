from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

if __name__ == '__main__':
    option = Options()
    option.add_experimental_option("detach", True)
    browser = wd.Chrome(options=option)
    browser.get("https://www.flipkart.com")
    banners_list = browser.find_elements(By.XPATH, "//*[@class ='_3bzdSa']//a")
    print(len(banners_list))
    for banner in banners_list:
        print(banner.get_attribute("href"))
        print(banner.get_attribute("innerHTML"))
        print(banner.get_attribute("outerHTML"))
        break
