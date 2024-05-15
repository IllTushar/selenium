from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    # option is used to inspect elements
    option = Options()
    option.add_experimental_option("detach", True)
    browser = wd.Chrome(options=option)
    browser.get("https://saya.net.in/")
    xpath = By.XPATH
    browser.implicitly_wait(10)  # implicit wait is used to find the element not attribute.. and it contain max time..
    # if element find between the time limit then it will continue other parts of the scripts .
    search_bar = browser.find_element(xpath, "//*[@placeholder='Search your Medicine by Composition or Brand']")
    search_bar.send_keys("telma")

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
