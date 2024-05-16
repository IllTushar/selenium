from authentication.Auth import AuthAutomation

if __name__ == '__main__':
    auth = AuthAutomation()
    auth.assets.url()
    auth.search_item()
    auth.product_and_add_medicine()
    auth.go_to_cart()
    auth.auth_auto_function(phone_number="7668270442")
