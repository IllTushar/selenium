from authentication.Auth import AuthAutomation
from assets.assets_file import Assets

if __name__ == '__main__':
    auth = AuthAutomation()
    # phone_number = input("Enter Phone Number +91: ")
    # auth.auth_auto_function(phone_number="9219736295")
    assets = Assets()
    assets.url()
    auth.search_item(assets, "xpath")
    auth.product_and_add_medicine(assets,"xpath")
