import pandas as pd

class place_order:

    def __init__(self, df_restaurant, df_customer, df_restaurant_capacity) -> None:
        self.df_restaurant = df_restaurant
        self.df_customer = df_customer
        self.df_restaurant_capacity = df_restaurant_capacity

    def order_by_restaurant(self):

        print("\n Please select one restaurant from below list.\n")
        print(self.df_restaurant_capacity.Name.to_string(index=False), "\n")
        
        restaurant_name = input("Type name of the restaurant: ").strip()
        filtered_data = self.df_restaurant[self.df_restaurant["Name"] == restaurant_name]
        print("\n",filtered_data[["Item", "Price"]])

        selected_items = input("Please type in the items you want to order, comma separated: ").strip()
        selected_items = list(map(str.strip,selected_items.split(",")))

        filtered_data = filtered_data[filtered_data["Item"].isin(selected_items)]

        print("\nBelow are the order details\n")
        print(filtered_data)

        print("Order successful")

        return filtered_data, restaurant_name
    
    def order_by_item(self):
        
        final_order = pd.DataFrame()

        print("\n Please select one item from below list.\n")
        item_list = self.df_restaurant.drop_duplicates(subset = "Item", keep = "first")

        stop_var = "N"
        while stop_var.lower().strip() != "y":

            print("\n", item_list["Item"].to_string(index=False), "\n")
            
            item_selection = input("Type the item you want to order: ").strip()
            filtered_data = self.df_restaurant[self.df_restaurant["Item"] == item_selection]
            print("\n", filtered_data)

            restaurant_selection = input("Please type in the restaurant name: ").strip()
            filtered_data = filtered_data[filtered_data["Name"] == restaurant_selection]

            final_order = final_order.append(filtered_data)
            print("\n", final_order, "\n")

            stop_var = input("press enter to order more items, press 'Y' to quit: ")

        print("Order successful")

        return final_order, restaurant_selection
