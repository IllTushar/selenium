from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    # option is used to inspect elements
    option = Options()
    option.add_experimental_option("detach", True)
    browser = wd.Chrome(options=option)
    browser.get("https://saya.net.in/")
    xpath = By.XPATH
    # explicit wait is used to wait the time wait element and it advantage over the implicit wait is that
    # we are define wait time for every element explicitly.
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((xpath, "//*[@placeholder='Search your Medicine by Composition or Brand']")))

    search_bar = browser.find_element(xpath, "//*[@placeholder='Search your Medicine by Composition or Brand']")
    search_bar.send_keys("telma")

    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((xpath, "//*[@role ='rowgroup']//a")))
    drug_list = browser.find_elements(xpath, "//*[@role ='rowgroup']//a")
    print(len(drug_list))
    for index, drug_name in enumerate(drug_list):
        print(
            f"The index of drug is ->{index + 1} and drug_name is-> {drug_name.get_attribute("href")} and text is -> {drug_name.text}")
        if "Telmisartan 20 Mg | Tablet" in drug_name.text:
            drug_name.click()
            break
        else:
            print("Nothing is present")

    action = wd.ActionChains(browser, duration=2000)
    action.move_to_element(
        browser.find_element(xpath, "//*[starts-with(@class ,'px-6 py-2 bg-lightOrange')]")).click().perform()

    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((xpath, '//*[@id="imageAndInfo"]/div/div[2]/div[4]/button/div/button[2]')))
    action.move_to_element(
        browser.find_element(xpath, '//*[@id="imageAndInfo"]/div/div[2]/div[4]/button/div/button[2]')).click().perform()
