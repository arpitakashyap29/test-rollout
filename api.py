from app import login, checkout, get_dashboard

def api_login(request):
    return login(request["username"], request["password"])

def api_checkout(request):
    return checkout(
        request["cart_id"],
        request["card_number"],
        request["cvv"],
        request["amount"]
    )

def api_dashboard(request):
    return get_dashboard(request["user_id"])