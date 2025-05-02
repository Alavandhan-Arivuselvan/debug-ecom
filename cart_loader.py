from discount_applier import apply_discounts

def load_cart():
    # In production, this could come from a database or frontend
    cart = [
        {"name": "Laptop", "price": 1500.0, "quantity": 1},
        {"name": "Mouse", "price": 40.0, "quantity": 2},
        {"name": "Keyboard", "price": 100.0, "quantity": 5}
    ]

    for item in cart:
        if not isinstance(item['price'], (int, float)) or item['price'] <= 0:
            raise ValueError(f"Invalid price in item: {item}")
        if not isinstance(item['quantity'], int) or item['quantity'] <= 0:
            raise ValueError(f"Invalid quantity in item: {item}")

    coupon_code = "BULK5"  # Simulated input, e.g., from user selection
    return apply_discounts(cart, coupon_code)
