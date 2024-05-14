import time
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    option = Options()
    option.add_experimental_option("detach", True)
    browser = wd.Chrome(options=option)
    browser.get('https://www.w3schools.com/python/ref_func_map.asp')
    time.sleep(3)
    element = browser.find_elements(By.XPATH, "//*[starts-with(@class ,'w3-btn w3-margin-bott')]")
    print(len(element))
    for number_of_element in element:
        number_of_element.click()
    print("Done")
