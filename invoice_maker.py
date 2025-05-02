from datetime import datetime

def make_invoice(total, cart, applied_coupon):
    invoice = {
        "metadata": {
            "created_at": datetime.utcnow().isoformat() + "Z",
            "coupon_used": applied_coupon,
            "items_count": sum(item['quantity'] for item in cart),
        },
        "items": cart,
        "total": round(total, 2)
    }
    Return invoice
