from controllers import get_customer_profile, get_order_details

def api_get_customer(request):
    customer_id = request.get("customer_id")
    return get_customer_profile(customer_id)

def api_get_order(request):
    order_id = request.get("order_id")
    return get_order_details(order_id)
