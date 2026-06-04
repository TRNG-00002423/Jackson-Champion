class Product:
    """A product in the inventory.

    Must implement these dunder methods:
        __str__     — "Laptop ($999.99) — 15 in stock"
        __repr__    — "Product('Laptop', 999.99, stock=15, category='electronics')"
        __eq__      — Equal if same name AND category
        __lt__      — Compare by price (enables sorting)
        __hash__    — Based on name + category (enables use in sets)
        __bool__    — True if in stock (stock > 0)
        __contains__ — Check if substring in product name

    Class attributes:
        total_products (int): Count of all Product instances
    """
    total_products = 0
    
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        Product.total_products += 1
    
    def __str__(self):
        return f"{self.name} (${self.price}) — {self.stock} in stock"
    
    def __repr__(self):
        return f"Product('{self.name}', {self.price}, stock={self.stock}, category='{self.category}')"
    
    def __eq__(self, other):
        return self.name == other.name and self.category == other.category
    
    def __lt__(self, other):
        return self.price < other.price
    
    def __hash__(self):
        return hash((self.name, self.category))
    
    def __bool__(self):
        if self.stock > 0:
            return True
        else:
            return False
    
    def __contains__(self, substring):
        if substring.lower() in self.name.lower(): #Change to lower case for comparison
            return True
        else:
            return False
    

#p1 = Product("Laptop", 999.99, 15, "electronics")
#p2 = Product("Laptop", 1099.99, 5, "electronics")
#p3 = Product("Mouse", 29.99, 50, "electronics")

#print(p1)                    # Laptop ($999.99) — 15 in stock
#print(repr(p1))              # Product('Laptop', 999.99, stock=15, category='electronics')
#print(p1 == p2)              # True (same name + category)
#print(p1 < p3)               # False (999.99 > 29.99)
#print(sorted([p1, p3]))      # Sorted by price
#print(bool(p1))              # True (in stock)
#print("laptop" in p1)        # True (case-insensitive search)
#print({p1, p2})              # Set with ONE item (they're equal)