#Comprehensions are a pythonic way to transform and filter data

#calculate squares of number from 0 to 9

for num in range(10): 
    sqr = num ** 2
    print(sqr)
    
squares = [x**2 for x in range(10)]
print(squares) #print as a list/dictionary/set etc

even_sq= [x**2 for x in range (10) if x % 2 == 0]
print(even_sq)

names = ["Alice", "Bob", "Charlie"]
#{'Alice': 5, 'Bob':3, 'Charlie":7'}

name_lengh = {name:len(name) for name in names}