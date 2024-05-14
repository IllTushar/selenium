from selenium import webdriver as wd
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    options = Options()
    options.add_experimental_option("detach", True)
    browser = wd.Chrome(options=options)
    browser.get("https://saya.net.in")
    search_bar = browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/section[1]/div[2]/div[1]/div/input')
    search_bar.send_keys("Telma")
    time.sleep(3)
    branded = browser.find_element(By.XPATH,
                                   '//*[@id="root"]/div[1]/section[1]/div[2]/div[1]/div/section/div/div/div[1]/button[2]')
    branded.click()
    time.sleep(3)
    search_bar.clear()
    download_app = browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/section[1]/div[1]/div/div/a[5]/p')
    print(download_app.text)
