from selenium import webdriver as wd
import time 

def routes(routes_list):
    browser = wd.Chrome()
    for route in routes_list:
        browser.get(route)
        print(browser.title)
        time.sleep(2)
    browser.quit()


if __name__=="__main__":
    routes_list = ["https://www.amazon.in","https://www.google.com","https://www.saya.net.in"]
    routes(routes_list)
    
    


   
    

