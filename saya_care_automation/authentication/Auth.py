from selenium.webdriver.common.by import By
from saya_care_automation.assets.assets_file import Assets


class AuthAutomation:
    def auth_auto_function(self, phone_number):
        assets = Assets()
        assets.url()
        xpath = By.XPATH

        # open login window
        login_x_path = "//*[text()='Login']"
        assets.explict_wait(5, xpath, login_x_path)
        login = assets.single_element_find(xpath, login_x_path)
        login.click()

        # set phone_number in phone number field
        phone_number_x_path = "//*[starts-with(@placeholder , '12345')]"
        assets.explict_wait(5, xpath, phone_number_x_path)
        phone_number_field = assets.single_element_find(xpath, phone_number_x_path)
        phone_number_field.send_keys(phone_number)

        # get otp button
        otp_button_file_path = "//*[text()='GET OTP']"
        assets.explict_wait(5, xpath, otp_button_file_path)
        otp_button = assets.single_element_find(xpath, otp_button_file_path)
        otp_button.click()

        # OTP
        otp = input("Enter OTP (note use '-' between every digit) : ")
        if otp is not None:
            otp_x_path = "//*[starts-with(@aria-label,'Please enter OTP character')]"
            assets.explict_wait(5, xpath, otp_x_path)
            otp_boxes = assets.multiple_element_find(xpath, otp_x_path)
            print(len(otp_boxes))
            for index, otp_box in enumerate(otp_boxes):
                split = otp.split("-")
                otp_box.send_keys(split[index])
        else:
            print("OTP is null")

        # Submit OTP
        submit_otp_x_path = '//*[text()="Submit"]'
        assets.explict_wait(5, xpath, submit_otp_x_path)
        submit_otp = assets.single_element_find(xpath, submit_otp_x_path)
        submit_otp.click()

        # go to search bar
        self.search_item(assets, xpath)

    def search_item(self, assets, xpath):
        # search medicine
        search_item_x_path = "//*[starts-with(@placeholder,'Search your Medicine')]"
        assets.explict_wait(5, xpath, search_item_x_path)
        search = assets.single_element_find(xpath, search_item_x_path)
        search.send_keys("telma")

        # go to product page
        product_list_x_path = "//*[@role ='rowgroup']//a"
        assets.explict_wait(5, xpath, product_list_x_path)
        drug_list = assets.multiple_element_find(xpath, product_list_x_path)
        if drug_list is not None:
            print(len(drug_list))
            for index, drug_name in enumerate(drug_list):
                if "Telmisartan 20 Mg | Tablet" in drug_name.text:
                    drug_name.click()
                    break
        else:
            print("Search medicine is not available!!")

        # go to product page
        self.product_and_add_medicine(assets, xpath)

    def product_and_add_medicine(self, assets, xpath):
        # add medicine
        medicine_x_path = "//*[starts-with(@class ,'px-6 py-2 bg-lightOrange')]"
        assets.explict_wait(20, xpath, medicine_x_path)
        medicine_add = assets.single_element_find(xpath, medicine_x_path)
        medicine_add.click()
