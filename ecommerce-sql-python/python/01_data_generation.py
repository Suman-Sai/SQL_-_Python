import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path

# -----------------------------
# SETTINGS
# -----------------------------
np.random.seed(42)
fake = Faker("en_IN")
Faker.seed(42)

# Number of records
NUM_CUSTOMERS = 5000
NUM_PRODUCTS = 500
NUM_ORDERS = 25000

# Create data folder
DATA_DIR = Path("../data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# 1. CUSTOMERS
# -----------------------------
customers = []

for i in range(1, NUM_CUSTOMERS + 1):

    customers.append({
        "customer_id": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": np.random.choice(["Male", "Female"]),
        "age": np.random.randint(18, 70),
        "city": fake.city(),
        "state": np.random.choice([
            "Telangana",
            "Karnataka",
            "Tamil Nadu",
            "Maharashtra",
            "Delhi",
            "Gujarat",
            "Kerala",
            "West Bengal",
            "Rajasthan",
            "Andhra Pradesh"
        ]),
        "country": "India",
        "signup_date": fake.date_between(
            start_date="-5y",
            end_date="-30d"
        ),
        "customer_segment": np.random.choice([
            "Regular",
            "Premium",
            "VIP"
        ])
    })

customers_df = pd.DataFrame(customers)

# -----------------------------
# 2. PRODUCTS
# -----------------------------
products = []

categories = {
    "Electronics": ["Mobile", "Laptop", "Headphones", "Tablet"],
    "Fashion": ["Shirt", "Jeans", "Shoes", "Saree"],
    "Home": ["Furniture", "Kitchen", "Decor"],
    "Beauty": ["Skincare", "Makeup", "Haircare"],
    "Sports": ["Fitness", "Cricket", "Football"]
}

for i in range(1, NUM_PRODUCTS + 1):

    category = np.random.choice(list(categories.keys()))
    subcategory = np.random.choice(categories[category])

    unit_cost = round(np.random.uniform(200, 30000), 2)
    unit_price = round(unit_cost * np.random.uniform(1.2, 2.0), 2)

    products.append({
        "product_id": i,
        "product_name": f"{subcategory} Product {i}",
        "category": category,
        "subcategory": subcategory,
        "brand": np.random.choice([
            "Brand A",
            "Brand B",
            "Brand C",
            "Brand D",
            "Brand E"
        ]),
        "unit_cost": unit_cost,
        "unit_price": unit_price
    })

products_df = pd.DataFrame(products)

# -----------------------------
# 3. ORDERS
# -----------------------------
orders = []

for i in range(1, NUM_ORDERS + 1):

    order_date = fake.date_between(
        start_date="-2y",
        end_date="-7d"
    )

    shipping_date = pd.to_datetime(order_date) + pd.Timedelta(
        days=np.random.randint(1, 8)
    )

    orders.append({
        "order_id": i,
        "customer_id": np.random.randint(1, NUM_CUSTOMERS + 1),
        "order_date": order_date,
        "shipping_date": shipping_date.date(),
        "order_status": np.random.choice([
            "Delivered",
            "Delivered",
            "Delivered",
            "Delivered",
            "Shipped",
            "Processing",
            "Cancelled"
        ]),
        "shipping_city": fake.city(),
        "shipping_state": np.random.choice([
            "Telangana",
            "Karnataka",
            "Tamil Nadu",
            "Maharashtra",
            "Delhi",
            "Gujarat",
            "Kerala",
            "West Bengal",
            "Rajasthan",
            "Andhra Pradesh"
        ])
    })

orders_df = pd.DataFrame(orders)

# -----------------------------
# 4. ORDER ITEMS
# -----------------------------
order_items = []

item_id = 1

for _, order in orders_df.iterrows():

    number_of_products = np.random.randint(1, 5)

    selected_products = np.random.choice(
        products_df["product_id"],
        size=number_of_products,
        replace=False
    )

    for product_id in selected_products:

        product = products_df[
            products_df["product_id"] == product_id
        ].iloc[0]

        order_items.append({
            "order_item_id": item_id,
            "order_id": order["order_id"],
            "product_id": product_id,
            "quantity": np.random.randint(1, 6),
            "unit_price": product["unit_price"],
            "discount": np.random.choice([
                0,
                0.05,
                0.10,
                0.15,
                0.20
            ])
        })

        item_id += 1

order_items_df = pd.DataFrame(order_items)

# -----------------------------
# 5. PAYMENTS
# -----------------------------
payments = []

for _, order in orders_df.iterrows():

    order_items_for_order = order_items_df[
        order_items_df["order_id"] == order["order_id"]
    ]

    amount = (
        order_items_for_order["quantity"]
        * order_items_for_order["unit_price"]
        * (1 - order_items_for_order["discount"])
    ).sum()

    payments.append({
        "payment_id": order["order_id"],
        "order_id": order["order_id"],
        "payment_date": pd.to_datetime(order["shipping_date"]).strftime("%Y-%m-%d"),"payment_date": order["shipping_date"],
        "payment_method": np.random.choice([
            "UPI",
            "Credit Card",
            "Debit Card",
            "Net Banking",
            "Cash on Delivery"
        ]),
        "payment_status": (
            "Refunded"
            if order["order_status"] == "Cancelled"
            else np.random.choice([
                "Paid",
                "Paid",
                "Paid",
                "Pending",
                "Failed"
            ])
        ),
        "payment_amount": round(amount, 2)
    })

payments_df = pd.DataFrame(payments)

# -----------------------------
# SAVE CSV FILES
# -----------------------------
customers_df.to_csv(DATA_DIR / "customers.csv", index=False)
products_df.to_csv(DATA_DIR / "products.csv", index=False)
orders_df.to_csv(DATA_DIR / "orders.csv", index=False)
order_items_df.to_csv(DATA_DIR / "order_items.csv", index=False)
payments_df.to_csv(DATA_DIR / "payments.csv", index=False)

# -----------------------------
# SUCCESS MESSAGE
# -----------------------------
print("===================================")
print("DATA GENERATION COMPLETED!")
print("===================================")

print("Customers:", len(customers_df))
print("Products:", len(products_df))
print("Orders:", len(orders_df))
print("Order Items:", len(order_items_df))
print("Payments:", len(payments_df))

print("\nCSV files created inside the data folder.")