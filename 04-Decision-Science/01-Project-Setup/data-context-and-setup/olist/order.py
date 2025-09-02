import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from olist.utils import haversine_distance
from olist.data import Olist

class Order:
    '''
    DataFrames containing all orders as index,
    and various properties of these orders as columns
    '''
    def __init__(self):
        # Assign an attribute ".data" to all new instances of Order
        self.data = Olist().get_data()

    def get_wait_time(self, is_delivered=True):
        """
        Returns a DataFrame with:
        [order_id, wait_time, expected_wait_time, delay_vs_expected, order_status]
        and filters out non-delivered orders unless specified
        """
        # Hint: Within this instance method, you have access to the instance of the class Order in the variable self, as well as all its attributes
        
        orders = self.data['orders'].copy()
        orders_delivered = orders[orders['order_status'] == "delivered"].copy()

        time_cols = ['order_purchase_timestamp','order_approved_at', 'order_delivered_carrier_date',              'order_delivered_customer_date', 'order_estimated_delivery_date']
        
        orders_delivered[time_cols] = orders_delivered[time_cols].apply(pd.to_datetime)
        
         # compute wait time
        orders_delivered['wait_time'] = orders_delivered['order_delivered_customer_date'] -         orders_delivered['order_purchase_timestamp']
        
        orders_delivered['wait_time'] = orders_delivered['wait_time'].dt.days
        
        # compute expected wait time
        orders_delivered['expected_wait_time'] = orders_delivered['order_estimated_delivery_date'] -         orders_delivered['order_purchase_timestamp']
        
        orders_delivered['expected_wait_time'] = orders_delivered['expected_wait_time'].dt.days
        
        # compute delay_vs_expected
        orders_delivered['delay_vs_expected'] = orders_delivered['order_delivered_customer_date']   -     orders_delivered['order_estimated_delivery_date']
        
        orders_delivered['delay_vs_expected'] = orders_delivered['delay_vs_expected'].dt.days
        
        orders_delivered['delay_vs_expected'] = np.where(orders_delivered['delay_vs_expected'] < 1,0,                         orders_delivered['delay_vs_expected'])
        
        orders_delivered = orders_delivered[[
            'order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected','order_status']]

        return orders_delivered

    def get_review_score(self):
         
            reviews = self.data['order_reviews'].copy()
            
            reviews['dim_is_five_star'] =  np.where(reviews['review_score'] == 5,1,0)
            reviews['dim_is_one_star'] =  np.where(reviews['review_score'] == 1,1,0)
            reviews = reviews[['order_id', 'dim_is_five_star', 'dim_is_one_star', 'review_score']]
            
            return reviews


    def get_number_items(self):
        """
        Returns a DataFrame with:
        order_id, number_of_items
        """
        orders_item = self.data['order_items'].copy()
        orders_item2 = orders_item.groupby(['order_id']).count().reset_index()
        orders_item_final = orders_item2[['order_id','order_item_id']]
        orders_item_final.rename(columns={"order_item_id": "number_of_items"},  inplace=True)
        
        return orders_item_final
        

    def get_number_sellers(self):
        """
        Returns a DataFrame with:
        order_id, number_of_sellers
        """
        order_items2 = self.data['order_items'].copy()
        order_items3 = order_items2[['order_id', 'seller_id']]
        orders_num_sellers = order_items3.groupby(['order_id']).count().reset_index()
        orders_num_sellers.rename(columns={"seller_id": "number_of_sellers"}, inplace=True)
        
        return orders_num_sellers
     

    def get_price_and_freight(self):
        """
        Returns a DataFrame with:
        order_id, price, freight_value
        """
        order_items_freight = self.data['order_items'][['order_id','price','freight_value']].copy()
        order_items_freight =  order_items_freight.groupby(by=["order_id"]).sum().reset_index()
          
        return order_items_freight
        
   

    # Optional
    def get_distance_seller_customer(self):
        """
        Returns a DataFrame with:
        order_id, distance_seller_customer
        """
        pass  # YOUR CODE HERE

    def get_training_data(self,
                          is_delivered=True,
                          with_distance_seller_customer=False):
        """
        Returns a clean DataFrame (without NaN), with the all following columns:
        ['order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected',
        'order_status', 'dim_is_five_star', 'dim_is_one_star', 'review_score',
        'number_of_items', 'number_of_sellers', 'price', 'freight_value',
        'distance_seller_customer']
        """
        # Hint: make sure to re-use your instance methods defined above
        
        
        training_set = self.get_wait_time(is_delivered).merge(self.get_review_score(), how='inner', on='order_id').merge(      self.get_number_items(), how='inner', on='order_id').merge(self.get_number_sellers(), how='inner', on='order_id').merge(    self.get_price_and_freight(), how='inner', on='order_id')
        
        return training_set.dropna()
