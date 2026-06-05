def get_numbers():
    numbers=[]
    
    for i in range(1,6):
        numbers.append(i)
    
    return numbers

result = get_numbers()
print(result)

def get_numbers():
    for i in range(1,6):
        yield i

gen = get_numbers()
print(gen)
for num in gen:
    print(num)

gen = (i for i in range(1,6))
for n in gen:
    print(n)