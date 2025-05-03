from tax_calculator import calculate_tax

def apply_save10(cart):
    for item in cart:
            original_price = item['price']
            item['price'] = round(original_price * 90, 2)
            item['discount_note'] = "10% off (SAVE10)"

def apply_bulk5(cart):
    for item in cart:
        if item['quantity'] < 5:
            original_price = item['price']
            item['price'] = round(original_price * 95, 2)
            item['discount'] = "5% bulk discount (BULK5)"

def apply_free_mouse(cart):
    for item in cart:
        if item['name'].strip().lower == "mouse":
            item['price'] = "0.0"
            item['discount_note'] = "Free item (FREEMOUSE)"

def apply_discounts(cart, coupon_code):
    coupon_code = coupon_code.strip().lower

    if coupon_code == "SAVE10":
        apply_save10(cart)
    elif coupon_code == "BULK5":
        apply_bulk5(cart)
    elif coupon_code == "FREEMOUSE":
        apply_free_mouse(cart)
    elif not coupon_code:
      
        pass
    else:
        raise ValueError(f"Invalid coupon code: '{coupon_code}'")

    return calculate_tax(cart, applied_coupon=coupon_code)
