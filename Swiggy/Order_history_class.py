
class order_history:

    def __init__(self, df_order_history) -> None:
        self.df_order_history = df_order_history

    def update_order_history(self,customer_name, order_details):
        
        order_details.rename(columns = {'Name':'Restaurant_name'}, inplace = True)
        order_details["Name"] = customer_name

        order_details = order_details[["Name", "Restaurant_name", "Item", "Price"]]

        print(order_details)

        self.df_order_history = self.df_order_history.append(order_details) 

    
    def show_order_history(self,customer_name):

        filtered_data = self.df_order_history[self.df_order_history["Name"] == customer_name]
        
        print(filtered_data)
