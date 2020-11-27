import pandas as pd

class customer:

    def __init__(self, df_restaurant, df_customer, df_restaurant_capacity) -> None:
        self.df_restaurant = df_restaurant
        self.df_customer = df_customer
        self.df_restaurant_capacity = df_restaurant_capacity


    def customer_login(self):
        customer_name = input("\nPlease type your name here to login: ").strip().lower()

        if self.df_customer["Name"].str.lower().str.contains(customer_name).any():
            print("\nLogin successful!\n")
            return customer_name
        else:
            print("\nThis name is not registered with us.")
            want_signup = input("\nIf you want to signup please type 'y': ")

            if want_signup.lower() == "y":
                self.customer_signup(customer_name)
                self.customer_login()
            else:
                print("Login unsuccessful")
                return False


    def customer_signup(self,customer_name):
        df_new_customer = pd.DataFrame([[customer_name,pd.NA]],columns=["Name","Order History"])
        self.df_customer = self.df_customer.append(df_new_customer,ignore_index=True)

