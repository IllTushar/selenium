from selenium import webdriver as wd 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
if __name__ == "__main__":
    options = Options()
    options.add_experimental_option("detach", True)
    # Create a WebDriver instance (you need to have the appropriate WebDriver installed, e.g., chromedriver for Chrome)
    browser = wd.Chrome(options=options)

    # Navigate to a webpage
    browser.get("https://saya.net.in")

    # Wait for the element to be clickable
    time.sleep(3)  # You can replace this with a more robust waiting mechanism such as WebDriverWait

    # Find the element using a CSS selector
    element = browser.find_element(By.XPATH, "//*[@name ='topic']")
    element.send_keys("Telma")



    # Close the browser
   # browser.quit()
