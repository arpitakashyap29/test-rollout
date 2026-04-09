from orders import place_order, cancel_order
from auth import login, verify_token

def api_login(request):
    return login(request["username"], request["password"])

def api_place_order(request):
    return place_order(
        request["user_id"],
        request["product_id"], 
        request["token"]
    )

def api_cancel_order(request):
    return cancel_order(request["order_id"])
