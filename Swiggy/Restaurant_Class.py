import pandas as pd

class restaurant:

    def __init__(self,df_restaurant,df_restaurant_capacity) -> None:
        self.df_restaurant = df_restaurant
        self.df_restaurant_capacity = df_restaurant_capacity
        
    def add_restaurant_from_user_input(self):
        """
        This functions will take the data from name
        and menu details from the owner of business 
        """
        # Creating a blank dataframe
        df_new_restaurant = pd.DataFrame(columns=[pd.DataFrame(columns=["Name", "Item", "Price"])])
        item_and_price_dict = {}

        print("To add your business please provide below details. \n")

        Name_of_restaurant = input("Name of the restaurant: ")
        processing_capacity = int(input("Please provide processing capacity 'between 1-5': "))

        stop_var = "N"
        while stop_var.lower().strip().strip() != "y":
            item_and_price  = input("Please give item name and price, comma seprated:")
            item_and_price = item_and_price.split(",")
            item_and_price_dict[item_and_price[0]] = int(item_and_price[1].strip())

            stop_var = input("press enter to add antother item, press 'Y' to quit: ")

        # creating the data frame
        items_series = pd.Series(item_and_price_dict)
        df_new_restaurant = pd.DataFrame(items_series)
        df_new_restaurant = df_new_restaurant.reset_index()
        df_new_restaurant["Name"] = Name_of_restaurant.strip()
        df_new_restaurant = df_new_restaurant.rename(columns={"index":"Item", 0:"Price"})
        df_new_restaurant = df_new_restaurant[["Name","Item","Price"]]

        # adding the data into the restaurant list
        self.df_restaurant = self.df_restaurant.append(df_new_restaurant, ignore_index=True)

        # adding processing capacity 
        restaurant_to_add = [[Name_of_restaurant,processing_capacity]]
        restaurant_to_add = pd.DataFrame(restaurant_to_add,columns=["Name","Capacity"])
        self.df_restaurant_capacity = self.df_restaurant_capacity.append(restaurant_to_add, ignore_index=True)


    def restaurant_menu_update(self):

        print("\nYou can change the menu of the restaurant here. \n")

        restaurant_name = input("Please provide the name of the restaurant: ").strip()
        filtered_data = self.df_restaurant[self.df_restaurant["Name"] == restaurant_name]

        print(filtered_data)
        print("\nPlease select below option to choose one operation\n")
        operation_type = input("""Press '1' to Add items 
                                Press '2' to Remove items
                                Press '3' to change processing capacity
                                Press 'Q' to quite
                                    
                                Please type one option here: """)
        
        while operation_type.lower().strip() != "q":

            if operation_type.lower().strip() == "1":
                item_name = input("Please provide item name and price separated by comma: ")
                item_name, price = item_name.split(",")            
                self.add_item_to_menu(restaurant_name, item_name, price)
            
            elif operation_type.lower().strip() == "2":
                item_name = input("Please provide item name: ")            
                self.remove_item_from_menu(restaurant_name,item_name)

            elif operation_type.lower().strip() == "3":
                changed_capacity = int(input("Please provide new processing capacity 'between 1-5': "))            
                self.change_processing_capacity(restaurant_name,changed_capacity)
            
            operation_type = input("""Press '1' to Add items 
                                        Press '2' to Remove items
                                        Press '3' to change processing capacity
                                        Press 'Q' to quit
                                        
                                        Please type one option here: """)
    
    def add_item_to_menu(self,restaurant_name,item_name,price):
        item_list = [[restaurant_name,item_name,price]]
        df_item_add = pd.DataFrame(item_list,columns=["Name","Item","Price"])
        self.df_restaurant = self.df_restaurant.append(df_item_add)


    def remove_item_from_menu(self,restaurant_name,item_name):
        self.df_restaurant = self.df_restaurant.drop(self.df_restaurant
                                                [
                                                    (self.df_restaurant["Name"] == restaurant_name) & 
                                                    (self.df_restaurant["Item"] == item_name)
                                                ].index)

    def change_processing_capacity(self,restaurant_name,changed_capacity):
        self.df_restaurant_capacity.loc[self.df_restaurant_capacity["Name"] == restaurant_name,"Capacity"] = changed_capacity
        print("The processing capacity of", restaurant_name,"has been changed to", str(changed_capacity))
