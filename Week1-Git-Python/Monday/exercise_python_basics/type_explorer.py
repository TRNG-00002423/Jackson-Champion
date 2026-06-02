
age = 28
price = 19.99
name = "Alice"
is_active = True
result = None

print("Variable Explanation:")
print(f"age = {age}                 Type: int")
print(f"price = {price}            Type: float")
print(f"name = {name}             Type: str")
print(f"is active = {is_active}         Type: bool")
print(f"result = {result}            Type: NoneType")

print("\nOperators Demo:")
print(f"17 // 5 = {17 // 5}                        Type: Floor Division")
print(f"17 / 5 = {17 / 5}                      Type: True Division")
print(f"{"QA " * 3}                Type: String Multiplication")
print(f"True + True = {is_active + is_active}             Type: Boolean Arithmetic")

print("\nPrecision Gotchas:")
print(f"0.1 + 0.2 = {0.1 + 0.2}                 Type: Floating-point Precision Issue")

print("\n == vs is:")
a = [1, 2, 3]
b = [1, 2, 3]

print(f"a == b: {a == b}            Values are equal)")
print(f"a is b: {a is b}            Objects are in different memory locations)")

