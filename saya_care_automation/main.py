from automation_script.automation_file import AuthAutomation
if __name__ == '__main__':
    auth = AuthAutomation()
    phone_num = "9999999999"

    auth.assets.url()
    auth.search_item()
    auth.product_and_add_medicine()
    auth.go_to_cart()
    auth.auth_auto_function(phone_number=phone_num)
    auth.checkout()
    auth.place_order()
