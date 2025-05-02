from totalizer import totalize

def calculate_tax(cart, applied_coupon, tax_rate=0.08):
    if not 0 <= tax_rate <= 1:
        raise ValueError(f"Invalid tax rate: {tax_rate}")

    for item in cart:
        base_price = item.get('price')
        if base_price is None:
            raise ValueError(f"Missing price in item: {item}")
        tax_amount = base_price * tax_rate
        item['price'] = round(base_price + tax_amount, 2)
        item['tax_applied'] = round(tax_amount, 2)

    return totalize(cart, applied_coupon)
