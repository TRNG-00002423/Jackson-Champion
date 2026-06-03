
tests = ["login", "search", "checkout", "logout"]

for test in tests:
    print(f'{test.upper()}')
    
numbers = [4, 5, 7, 2, -5, 9, -2, 5, -3, 1, 0, 8]
for num in numbers:
    if num > 0:
        print(num)
    elif num < 0:
        print(f'{num} is negative, skipping...')
        continue
    if num == 0:
        print('Zero found, stopping...')
        break