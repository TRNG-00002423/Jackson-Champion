class MathUtil:
    
    def __init__(self):
        pass
    
    @staticmethod # neither self nor cls
    def is_even(n):
        return n % 2 == 0
    
    def cel_to_fer(c):
        return c * (9/5) + 32
    
mu = MathUtil()
print(mu.is_even(20))
