numbers = [1,2,3,4,5] # list -- iterable

for number in numbers:
    print(number)
    
#next(numbers)

print("------------")
my_itr = iter(numbers) # Create an interator

print(next(my_itr))
print(next(my_itr))
next(my_itr)