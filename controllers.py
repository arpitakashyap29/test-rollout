from utility import fetch_customer, fetch_order

def get_customer_profile(customer_id: str):
    # Passes string but utility now expects int
    return fetch_customer(customer_id)

def get_order_details(order_id: str):
    # Passes string but utility now expects int  
    return fetch_order(order_id)

def get_customer_orders(customer_id: str, order_id: str):
    customer = fetch_customer(customer_id)
    order = fetch_order(order_id)
    return {"customer": customer, "order": order}
