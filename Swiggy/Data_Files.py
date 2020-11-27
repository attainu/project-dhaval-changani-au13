import pandas as pd # file I/O
import os

##########################
# Below is the initialization of the main code
# this will create all the necessary files that will hold our app data
class data_files_class():


    def __init__(self) -> None:
        self.current_working_directory = os.getcwd()
        self.dir_name = "Data Files"
        self.restaurant_csv  = "restaurant.csv"
        self.processing_capacity_csv  = "processing_capacity.csv"
        self.customer_csv = "customer.csv"
        self.order_history_csv = "order_history.csv"

    def create_folder(self):

        if not os.path.isdir(self.current_working_directory + "\\" + self.dir_name): # if the folder is not available 
            os.mkdir(self.current_working_directory + "\\" + self.dir_name) # this will create the folder named > Data Files

        self.data_files_path = os.path.join(self.current_working_directory, self.dir_name)


    def create_restaurant_file(self):

        df_restaurant = pd.DataFrame(columns=["Name", "Item", "Price"])
        restaurant_list = ["The Lady & Sons","Chez Panisse Cafe","Spago","Chipotle Mexican Grill","Vintage Machine ","Banana Leaf","Yum Yum Tree"]
        item_vs_price_dict  = {"Paneer butter masala" : 200,"Chevdo" : 200,"Dum aloo" : 250,"Pindi chana" : 250,"Kori rotti" : 300,"Zunka or Pitla" : 300,"Rajma chaval" : 350,"Aloo methi" : 400,"Amritsari fish" : 400,"Attu" : 400,"Goli bajje" : 400,"Undhiyu" : 400,"Gajar ka halwa" : 450,"Moong dal ka halwa" : 450,"Daal Dhokli" : 450,"Payasam" : 500,"Thengai sadam" : 500,"Locha" : 500,"Puli sadam" : 550,"Bhakri" : 550,"Pohe" : 550,"Imarti" : 600,"Dhokla" : 600,"Naan" : 650,"Samose" : 650,"Bonda" : 650,"Puri Bhaji" : 650,"Bhindi masala" : 700}

        for restaurant_name in restaurant_list:
            items_series = pd.Series(item_vs_price_dict)
            df_restaurant_temp = pd.DataFrame(items_series)
            df_restaurant_temp = df_restaurant_temp.reset_index()
            df_restaurant_temp["Name"] = restaurant_name
            df_restaurant_temp = df_restaurant_temp.rename(columns={"index":"Item", 0:"Price"})
            df_restaurant = df_restaurant.append(df_restaurant_temp)

        df_restaurant = df_restaurant.reset_index()
        del df_restaurant["index"]

        # creating a csv file
        df_restaurant.to_csv(self.data_files_path + "\\" + self.restaurant_csv,index=False) # creating a restaurant file


    def create_processing_capacity_file(self):

        #creating a file for processing capacity
        capacity_dict = {"The Lady & Sons" : 5,"Chez Panisse Cafe" : 6,"Spago" : 6,"Chipotle Mexican Grill" : 4,"Vintage Machine " : 5,"Banana Leaf" : 5,"Yum Yum Tree" : 3}
        items_series = pd.Series(capacity_dict)
        df_processing_capacity = pd.DataFrame(items_series)
        df_processing_capacity = df_processing_capacity.reset_index()
        df_processing_capacity = df_processing_capacity.rename(columns={"index":"Name",0:"Capacity"})

        # creating a csv file
        df_processing_capacity.to_csv(self.data_files_path + "\\" + self.processing_capacity_csv,index=False) # creating a restaurant file

    
    def create_customer_file(self):

        # if the file is not created check and create the file
        customer_name_list = ["James Mary","John Patricia","Robert Jennifer","Michael Linda","William Elizabeth","David Barbara","Richard Susan","Joseph Jessica","Thomas Sarah","Charles Karen","Christopher Nancy","Daniel Lisa","Matthew Margaret","Anthony Betty","Donald Sandra","Mark Ashley","Paul Dorothy","Steven Kimberly","Andrew Emily","Kenneth Donna"]
        customer_series = pd.Series(customer_name_list)
        df_customer = pd.DataFrame(customer_series,columns=["Name"])
        df_customer["Order History"] = pd.NA

        # creating a csv file
        df_customer.to_csv(self.data_files_path + "\\" + self.customer_csv,index=False) # creating a restaurant file


    def create_order_history_file(self):
        df_order_history = pd.DataFrame(columns=["Name", "Restaurant_name", "Item", "Price"])
        
        # creating a csv file
        df_order_history.to_csv(self.data_files_path + "\\" + self.order_history_csv,index=False) # creating a restaurant file


    def read_data_files(self):
        self.df_restaurant = pd.read_csv(self.data_files_path + "\\" + self.restaurant_csv)
        self.df_customer = pd.read_csv(self.data_files_path + "\\" + self.customer_csv)
        self.df_restaurant_capacity = pd.read_csv(self.data_files_path + "\\" + self.processing_capacity_csv)
        self.df_order_history = pd.read_csv(self.data_files_path + "\\" + self.order_history_csv) # creating a restaurant file

        return self.df_restaurant, self.df_customer, self.df_restaurant_capacity, self.df_order_history

    def export_data_files(self):
        self.df_restaurant.to_csv(self.data_files_path + "\\" + self.restaurant_csv,index=False)
        self.df_customer.to_csv(self.data_files_path + "\\" + self.customer_csv,index=False)
        self.df_restaurant_capacity.to_csv(self.data_files_path + "\\" + self.processing_capacity_csv,index=False)
        self.df_order_history.to_csv(self.data_files_path + "\\" + self.order_history_csv,index=False) # creating a restaurant file


if __name__ == "__main__":
    
    chandu = data_files_class()
    chandu.create_folder()
    chandu.create_order_history_file()
