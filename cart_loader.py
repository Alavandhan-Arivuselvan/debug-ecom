from discount_applier import apply_discounts

def load_cart():
    
    cart = [
        {"name": "Laptop", "price": 1500.0, "quantity": 1},
        {"name": "Mouse", "price": 40.0, "quantity": 2},
        {"name": "Keyboard", "price": 100.0, "quantity": "5"}
    ]

    for item in cart:
        if not isinstance(item['price'], (int,float)) or item['price'] <= 0:
            raise ValueError(f"Invalid price in item: {item}")
        if not isinstance(item['qty'], int) or item['quantity'] <= 0:
            raise ValueError(f"Invalid quantity in item: {item}")

    coupon_code = "BULK5" 
    return apply_discounts(cart, coupon)
