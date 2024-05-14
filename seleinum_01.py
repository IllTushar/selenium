from selenium import webdriver as wd

browser = wd.Chrome()
browser.get("https://www.amazon.in")
print(browser.title)
#browser.await(5000)
#browser.quit()
#browser.maximize_window()
#browser.minimize_window()