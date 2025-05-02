from cart_loader import load_cart

def format_currency(amount):
    return f"${amount:,.2f}"

def print_separator(char='-', length=60):
    print(char * length)

def main():
    try:
        invoice = load_cart()

        metadata = invoice['metadata']
        items = invoice['items']
        total = invoice['total']

        print_separator("=")
        print(f"{'INVOICE RECEIPT':^60}")
        print_separator("=")
        print(f"Date: {metadata['created_at']}")
        print(f"Coupon Applied: {metadata['coupon_used'] or 'None'}")
        print(f"Total Items: {metadata['items_count']}")
        print_separator()

      
        print(f"{'Item':<20} {'Qty':>5} {'Unit Price':>12} {'Tax':>8} {'Final Price':>12}")
        print_separator()

        for item in items:
            name = item['name']
            qty = item['quantity']
            price = format_currency(item['price'])
            tax = format_currency(item.get('tax_applied', 0))
            total_price = format_currency(item['price'] * qty)
            print(f"{name:<20} {qty:>5} {price:>12} {tax:>8} {total_price:>12}")
            if 'discount_note' in item:
                print(f"{'':<20} {'':>5} {'':>12} {'':>8} {'➤ ' + item['discount_note']:<12}")

        print_separator("=")
        print(f"{'TOTAL AMOUNT':>50}: {format_currency(total)}")
        print_separator("=")

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
