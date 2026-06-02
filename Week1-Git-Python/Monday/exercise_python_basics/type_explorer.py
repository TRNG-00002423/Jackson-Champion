
age = 28
price = 19.99
name = "Alice"
is_active = True
result = None

print("Variable Explanation:")
print(f"age = {age}                             Type: int")
print(f"price = {price}                        Type: float")
print(f"name = {name}                         Type: str")
print(f"is active = {is_active}                     Type: bool")
print(f"result = {result}                        Type: NoneType")

print("\nOperators Demo:")
print(f"17 // 5 = {17 // 5}                          Type: Floor Division")
print(f"17 / 5 = {17 / 5}                         Type: True Division")
print(f"\"QA \" * 3 = {"QA" * 3}                   Type: String Multiplication")
print(f"True + True = {is_active + is_active}                      Type: Boolean Arithmetic")

print("\nPrecision Gotchas:")
print(f"0.1 + 0.2 = {0.1 + 0.2}      Type: Floating-point Precision Issue")

print("\n== vs is:")

# a and b have the same values but are different objects in memory
a = [1, 2, 3]
b = [1, 2, 3]
c = a #c references the same object as a

print('a = [1, 2, 3]')
print('b = [1, 2, 3]')
print('c = a') # c references the same object as a

# a = b should return True while a is b should return False
print(f"\na == b: {a == b}                         Same Value?") 
print(f"a is b: {a is b}                        Same Object?")

# both should return True since a and c reference the same object and value
print(f"a == c: {a == c}                         Same Value?")
print(f"a is c: {a is c}                         Same Object?")
