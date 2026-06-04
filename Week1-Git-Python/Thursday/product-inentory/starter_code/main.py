"""
Product Inventory System — Main Program
Demonstrates the full system with exception handling.
"""

from product import Product
from inventory import Inventory
from exceptions import ProductNotFoundError, InsufficientStockError


def main():
    inv = Inventory()

    # 1. Add at least 8 products across 3+ categories
    products = [
        Product("Laptop", 999.99, 15, "electronics"),
        Product("Laptop", 1099.99, 5, "electronics"),
        Product("Mouse", 29.99, 50, "electronics"),
        Product("Protein Bar", 2.99, 0, "grocery"),
        Product("Office Chair", 129.99, 25, "office"),
        Product("Tomato", 0.67, 40, "grocery"),
        Product("Notebook", 4.99, 100, "office"),
        Product("Computer Monitor", 249.99, 12, "electronics"),
        Product("Ottoman", 365.99, 6, "furniture"),
        Product("Twin Bed", 300.65, 8, "furniture")
        
    ]

    for product in products:
        product_id = inv.add_product(product)
        print(f"Product ID {product_id}: {product}")
        
    # 2. Display all products (sorted by price)
    print("\n--- All Products Sorted by Price ---")
    for product in sorted(inv.products.values()):
        print(product)

    # 3. Search for products containing "pro"
    for product in inv.search("pro"):
        print(product)


    # 4. Show products in a specific category
    print("\n---Electronics ---")
    for product in inv.by_category("electronics"):
        print(product)
    
    print("\n---Grocery ---")
    for product in inv.by_category("grocery"):
        print(product)
    
    print("\n---Office ---")
    for product in inv.by_category("office"):
        print(product)
    
    print("\n---Furniture ---")
    for product in inv.by_category("furniture"):
        print(product)
    
    # 5. Sell products — include at least one that fails
    try:
        inv.sell(1, 3)   # Should succeed
        inv.sell(1, 999) # Should raise InsufficientStockError
    except InsufficientStockError as e:
        print(f"❌ {e}")
        print(f"   Requested: {e.requested}, Available: {e.available}")

    # 6. Try to access a product that doesn't exist
    try:
        inv.get_product(999)
    except ProductNotFoundError as e:
        print(f"❌ {e}")

    # 7. Show transaction history
    print("\n--- Transaction History ---")
    for entry in inv.history:
        print(entry)

    # 8. Show inventory summary (using comprehension-powered summary())
    print("\n--- Inventory Summary ---")
    summary = inv.summary()
    for key, value in summary.items():
        print(f"{key}: {value}")

    # 9. Use set operations on categories
    print("\n--- Category Set Operations ---")
    store_categories = inv.categories
    online_categories = {"electronics", "clothing", "books"}

    print(f"Store categories: {store_categories}")
    print(f"Online categories: {online_categories}")
    print(f"Union: {store_categories | online_categories}")
    print(f"Intersection: {store_categories & online_categories}")

    # 10. Use a tuple to store immutable product configurations
    print("\n--- Product Config Tuples ---")
    product_configs = (
        ("Tablet", 399.99, 10, "electronics"),
        ("Pen Pack", 5.99, 75, "office"),
    )

    for config in product_configs:
        print(config)


if __name__ == "__main__":
    main()