from selenium.webdriver.common.by import By
from saya_care_automation.assets.assets_file import Assets


class AuthAutomation:
    def __init__(self):
        self.assets = Assets()

    def auth_auto_function(self, phone_number):
        # open login window
        xpath = By.XPATH
        # login_x_path = "//*[text()='Login']"
        # self.assets.explict_wait(5, xpath, login_x_path)
        # login = self.assets.single_element_find(xpath, login_x_path)
        # login.click()

        # set phone_number in phone number field
        phone_number_x_path = "//*[starts-with(@placeholder , '12345')]"
        self.assets.explict_wait(5, xpath, phone_number_x_path)
        phone_number_field = self.assets.single_element_find(xpath, phone_number_x_path)
        phone_number_field.send_keys(phone_number)

        # get otp button
        otp_button_file_path = "//*[text()='GET OTP']"
        self.assets.explict_wait(5, xpath, otp_button_file_path)
        otp_button = self.assets.single_element_find(xpath, otp_button_file_path)
        otp_button.click()

        # OTP
        otp = input("Enter OTP (note use '-' between every digit) : ")
        if otp is not None:
            otp_x_path = "//*[starts-with(@aria-label,'Please enter OTP character')]"
            self.assets.explict_wait(5, xpath, otp_x_path)
            otp_boxes = self.assets.multiple_element_find(xpath, otp_x_path)
            print(len(otp_boxes))
            for index, otp_box in enumerate(otp_boxes):
                split = otp.split("-")
                otp_box.send_keys(split[index])
        else:
            print("OTP is null")

        # Submit OTP
        submit_otp_x_path = '//*[text()="Submit"]'
        self.assets.explict_wait(5, xpath, submit_otp_x_path)
        submit_otp = self.assets.single_element_find(xpath, submit_otp_x_path)
        submit_otp.click()

    # search medicine
    def search_item(self):
        xpath = By.XPATH
        search_item_x_path = "//*[starts-with(@placeholder,'Search your Medicine')]"
        self.assets.explict_wait(5, xpath, search_item_x_path)
        search = self.assets.single_element_find(xpath, search_item_x_path)
        search.send_keys("telma")

        # go to product page
        product_list_x_path = "//*[@role ='rowgroup']//a"
        self.assets.explict_wait(5, xpath, product_list_x_path)
        drug_list = self.assets.multiple_element_find(xpath, product_list_x_path)
        if drug_list is not None:
            print(len(drug_list))
            for index, drug_name in enumerate(drug_list):
                if "Telmisartan 20 Mg | Tablet" in drug_name.text:
                    drug_name.click()
                    break
        else:
            print("Search medicine is not available!!")

    # Add medicine
    def product_and_add_medicine(self):
        xpath = By.XPATH
        medicine_x_path = "//*[contains(@class ,'px-6') and contains(@class ,'py-2') and contains(@class ,'bg-lightOrange')]"
        add_med = self.assets.wait_until_element_not_click_able(xpath, medicine_x_path)
        add_med.click()

    # Go to cart
    def go_to_cart(self):
        xpath = By.XPATH
        cart_button_x_path = "//*[starts-with(@class,'text-4xl hover:scale-110')]"
        self.assets.explict_wait(5, xpath, cart_button_x_path)
        cart_btn = self.assets.single_element_find(xpath, cart_button_x_path)
        cart_btn.click()

    def add_address(self):
        pass

    # checkout button
    def checkout(self):
        xpath = By.XPATH
        proceed_to_checkout = "//*[text()='Proceed to Checkout']"
        self.assets.explict_wait(5, xpath, proceed_to_checkout)
        self.assets.mouse_hover(xpath, proceed_to_checkout)

    def place_order(self):
        xpath = By.XPATH

        # choose cod
        choose_code_x_path = '//*[@id = "cod_payment"]'
        self.assets.explict_wait(5, xpath, choose_code_x_path)
        click_on_cod = self.assets.single_element_find(xpath, choose_code_x_path)
        click_on_cod.click()

        # # place order
        place_order_x_path = '//*[text()="Place Order"]'
        self.assets.explict_wait(5, xpath, place_order_x_path)
        self.assets.mouse_hover(xpath, place_order_x_path)
