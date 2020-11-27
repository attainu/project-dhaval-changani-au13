import pandas as pd
import os

from Customer_class import customer
from Restaurant_Class import restaurant
from Data_Files import data_files_class
from Order_Class import place_order
from Capacity_class import capacity
from Order_history_class import order_history

def print_center(string_to_print = "\n"):
    print(string_to_print.center(os.get_terminal_size().columns))

# Welcome screen
print("\n \n \n ")
print_center("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print_center("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print_center("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print_center("Welcome to our food ordering app.")
print_center("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print_center("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print_center("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("\n \n \n ")

# First we will initialize the database
data_manager = data_files_class()
data_manager.create_folder()

create_files = input("""\nIf you are running this application first time,
                        \nPlease type 'Y' to initialise data files
                        \notherwise press any key: """)

if create_files.lower().strip() == "y":
    # one by one we will create all necessary files
    data_manager.create_restaurant_file()
    data_manager.create_customer_file()
    data_manager.create_processing_capacity_file()
    data_manager.create_order_history_file()

# loading data frame into the memory
df_restaurant, df_customer, df_restaurant_capacity, df_order_history = data_manager.read_data_files()

# login Screen
print("\nAre you a restaurant owner or a customer.\n")
print("Please select one option below")
chosen_mode = input("""
                    1. Restaurant owner
                    2. Customer

                    press 'Q' to exit.

                    Please type in you answer here: """).strip()

while chosen_mode.lower().strip() != "q":

    # if the chosen mode is restaurant
    if chosen_mode.strip().lower() == "1":
        restaurant_manager = restaurant(df_restaurant, df_restaurant_capacity)        
        print("\nBelow are the operations you can perform.")
        print("\nPlease select one option")        
        operation_selection = input("""
                                1. Add new restaurant
                                2. Update menu of a existing restaurant

                                press 'Q' to exit.

                                Please type in you answer here: """).strip().lower()

        while operation_selection.lower().strip() != "q":

            if operation_selection.lower().strip() == "1":
                restaurant_manager.add_restaurant_from_user_input()

            elif operation_selection.lower().strip() == "2":
                restaurant_manager.restaurant_menu_update()

            operation_selection = input("""
                                1. Add new restaurant
                                2. Update menu of a existing restaurant

                                press 'Q' to exit.

                                Please type in you answer here: """).strip()

    # if chosen mode is customer
    elif chosen_mode.strip().lower() == "2":
        customer_manager = customer(df_restaurant, df_customer, df_restaurant_capacity)
        
        login_status = customer_manager.customer_login()
        if login_status != False:
            
            order_again = "Y"
            while order_again.lower().strip() != "q":

                order_manager = place_order(df_restaurant, df_customer, df_restaurant_capacity)
                print("\n To place your order please select one of the options below.")
                order_selection = input("""
                                        1. Order by restaurant name
                                        2. Order by item name
                                        3. To view order history

                                        press 'Q' to go back

                                        Please type in you answer here: """).strip()
                    
                while order_selection.lower().strip() != "q":
                                                                                                                                                                                                    
                    if order_selection.lower().strip() == "1":
                        order_details, restaurant_name = order_manager.order_by_restaurant()
                        item_count  = len(order_details)
                        current_capacity = df_restaurant_capacity.loc[df_restaurant_capacity["Name"] == restaurant_name,"Capacity"].item()
                        
                        if current_capacity - item_count > 0:
                            
                            capacity_manager = capacity(df_restaurant_capacity,item_count,restaurant_name)
                            capacity_manager.reduce_capacity()

                            history_manager = order_history(df_order_history)
                            history_manager.update_order_history(login_status, order_details)

                        else:
                            print("\nThe restaurant is not able to process more than", 
                            str(current_capacity), "items at this time.")
                            print("Please order after some time.\n")

                        break

                    elif order_selection.lower().strip() == "2":
                        order_details, restaurant_name = order_manager.order_by_item()
                        item_count  = len(order_details)
                        current_capacity = df_restaurant_capacity.loc[df_restaurant_capacity["Name"] == restaurant_name,"Capacity"].item()
                        
                        if current_capacity - item_count > 0:
                            
                            capacity_manager = capacity(df_restaurant_capacity,item_count,restaurant_name)
                            capacity_manager.reduce_capacity()

                            history_manager = order_history(df_order_history)
                            history_manager.update_order_history(login_status, order_details)

                        else:
                            print("\nThe restaurant is not able to process more than", 
                            str(current_capacity), "items at this time.")
                            print("Please order after some time.\n")

                        break

                    elif order_selection.lower().strip() != "3":
                        history_manager = order_history(df_order_history)
                        history_manager.show_order_history(login_status)

                        break

                    order_selection = input("""
                                                    1. Order by restaurant name
                                                    2. Order by item name

                                                    press 'Q' to go back

                                                    Please type in you answer here: """).strip()
        
                order_again = input("\nTo order again press enter, to exit press 'Q': ")

    chosen_mode = input("""
                        1. Restaurant owner
                        2. Customer

                        press 'Q' to exit.

                        Please type in you answer here: """).strip()


# Finally we will export all the data to csv files
data_manager.export_data_files()

print_center("\nThank you for using our service.\n")
