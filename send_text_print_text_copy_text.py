from selenium import webdriver as wd
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    options = Options()
    options.add_experimental_option("detach",True)
    browser = wd.Chrome(options = options)
    browser.get("https://saya.net.in")