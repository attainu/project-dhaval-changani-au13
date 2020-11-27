from timer import *
import threading

class capacity():   

    def __init__(self,df_restaurant_capacity,item_count,restaurant_name) -> None:
        self.df_restaurant_capacity = df_restaurant_capacity
        self.item_count = item_count
        self.restaurant_name = restaurant_name

    def reduce_capacity(self):
        global current_capacity
        
        current_capacity = self.df_restaurant_capacity.loc[self.df_restaurant_capacity["Name"] == self.restaurant_name,"Capacity"]

        # changing the capacity 
        self.df_restaurant_capacity.loc[self.df_restaurant_capacity["Name"] == self.restaurant_name,"Capacity"] = current_capacity - self.item_count

        t = threading.Timer(15.0, self.increase_capacity)
        t.start()


    def increase_capacity(self):

        # changing the capacity back to original count
        self.df_restaurant_capacity.loc[self.df_restaurant_capacity["Name"] == self.restaurant_name,"Capacity"] = current_capacity

