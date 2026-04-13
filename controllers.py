from utility import fetch_customer, fetch_order

def get_customer_profile(customer_id: str):
    return fetch_customer(customer_id)

def get_order_details(order_id: str):
    return fetch_order(order_id)
