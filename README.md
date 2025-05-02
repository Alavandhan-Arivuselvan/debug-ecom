# 🛒 E-commerce Cart System

This project simulates a modular cart pipeline for an e-commerce platform. It models how a customer's shopping cart moves through stages like **loading**, **discount application**, **tax calculation**, **total computation**, and **invoice generation**, with each stage handled in a separate Python file.

---

## 📁 File Structure & Description

### `main.py`
**Role**: Entry point of the application  
**Responsibilities**:
- Triggers the cart pipeline.
- Receives the final invoice.
- Prints a clean, formatted bill-style receipt.
- Handles and displays any runtime errors.

---

### `cart_loader.py`
**Role**: Simulates cart loading and coupon input  
**Responsibilities**:
- Initializes the cart with items (normally would come from a DB or API).
- Validates item data (e.g., positive prices and quantities).
- Passes cart and coupon to the discount stage.

---

### `discount_applier.py`
**Role**: Applies coupon-based discounts  
**Responsibilities**:
- Supports multiple coupon types:
  - `SAVE10`: 10% off all items.
  - `BULK5`: 5% off items with quantity ≥ 5.
  - `FREEMOUSE`: Makes any item named "Mouse" free.
- Applies per-item logic for discounts.
- Adds a `discount_note` to affected items.
- Passes updated cart to the tax calculation stage.


---

### `tax_calculator.py`
**Role**: Adds tax to item prices  
**Responsibilities**:
- Applies a configurable tax rate (default 8%).
- Increases each item's price accordingly.
- Stores the applied tax amount per item.
- Passes the updated cart to the totalizer.

---

### `totalizer.py`
**Role**: Calculates the final total  
**Responsibilities**:
- Sums the post-tax price of all items (taking quantity into account).
- Validates data integrity.
- Passes the cart and final amount to the invoice generator.

---

### `invoice_maker.py`
**Role**: Generates a structured invoice  
**Responsibilities**:
- Combines cart, metadata (e.g. timestamp, coupon, item count), and total.
- Returns a dictionary representing the final bill.

---

## 📌 Features

- Modular, pipeline-style architecture (each stage in its own file).
- Error handling for invalid coupons and data.
- Realistic receipt formatting (aligned columns, discounts, tax shown).
- Easy to extend (e.g., add new coupons, external cart input, or export to PDF).

---

## ▶️ How to Run

```bash
python main.py
