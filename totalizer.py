from invoice_maker import make_invoice

def totalize(cart, applied_coupon):
    if not cart:
        raise ValueError("Cart is empty")

    total = 0.0
    for item in cart:
        price = item.get('price')
        qty = item.get('quantity')
        if price is None or qty is None:
            raise ValueError(f"Invalid item data: {item}")
        total += price * qty

    return make_invoice(total, cart, applied_coupon)
