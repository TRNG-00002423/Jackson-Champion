from collections import deque
from exceptions import ProductNotFoundError
from exceptions import InsufficientStockError
class Inventory:
    """A collection of products with search, filter, and transaction capabilities.

    Features:
        - Add/remove products
        - Search by name or category
        - Transaction history (deque with maxlen=50)
        - Restock and sell operations with exception handling
    """

    def __init__(self):
        self.products = {}          # {product_id: Product}
        self.categories = set()     # Unique categories
        self.history = deque(maxlen=50)  # Recent transactions
        self._next_id = 1

    def add_product(self, product):
        """Add a product to inventory. Return the assigned ID."""
        product_id = self._next_id
        self.products[product_id] = product
        self.categories.add(product.category)
        self._next_id += 1
        return product_id
        

    def remove_product(self, product_id):
        """Remove a product. Raise ProductNotFoundError if missing."""
        if product_id not in self.products:
            raise ProductNotFoundError(product_id)
        
        del self.products[product_id]

    def get_product(self, product_id):
        """Get a product by ID. Raise ProductNotFoundError if missing."""
        if product_id not in self.products:
            raise ProductNotFoundError(product_id)
        
        return self.products[product_id]
        

    def sell(self, product_id, quantity):        
        """Sell units of a product.
        Raise ProductNotFoundError if ID doesn't exist.
        Raise InsufficientStockError if not enough stock.
        Record transaction in history.
        """
        
        if product_id not in self.products:
            raise ProductNotFoundError(product_id)
        
        product = self.products[product_id]
        
        if product.stock < quantity:
            raise InsufficientStockError(
                product.name,
                quantity,
                product.stock
            )
        product.stock -= quantity
        
        self.history.append(f"Sold {quantity} units of {product.name}")

    def restock(self, product_id, quantity):
        
        """Add stock. Raise ProductNotFoundError if missing."""
        if product_id not in self.products:
            raise ProductNotFoundError(product_id)
        
        product = self.products[product_id]
        product.stock += quantity
        
        self.history.append(f"Restocked {quantity} units of {product.name}")
        

    # --- Comprehension-powered queries ---

    def search(self, keyword):
        """Return products containing keyword (case-insensitive).
        Use a list comprehension and the __contains__ dunder.
        """
        return [product for product in self.products.values() if keyword in product]

    def by_category(self, category):
        """Return products in a category. Use a list comprehension."""
        return [product for product in self.products.values() if product.category == category]

    def in_stock(self):
        """Return products with stock > 0. Use __bool__ dunder + filter."""
        return list(filter(bool, self.products.values()))

    def price_range(self, min_price, max_price):
        """Return products in the price range. Use a list comprehension."""
        return [product for product in self.products.values() if product.price >= min_price and product.price <= max_price]

    def summary(self):
        """Return a dict with:
        - total_products
        - total_value (sum of price * stock for each product)
        - categories (sorted list)
        - out_of_stock_count
        Use dict/list comprehensions.
        """
        return {"total_products" :len(self.products),
                "total_value" : sum(product.price * product.stock for product in self.products.values()),
                "categories" : sorted({product.category for product in self.products.values()}),
                "out_of_stock_count" : sum(1 for product in self.products.values() if product.stock == 0)}