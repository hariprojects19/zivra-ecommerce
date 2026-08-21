from .cart import Cart

def cart(request):#Django automatically injects cart into every template.
    return {'cart':Cart(request)}