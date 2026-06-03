def fizzbuzz(n):
    if n % 3 == 0 and n % 5 ==0 and n % 7 == 0:
        return "FizzBuzzBoom"
    elif n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0 and n % 7 == 0:
        return "FizzBoom"
    elif n % 5 == 0 and n % 7 == 0:
        return "BuzzBoom"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 7 == 0:
        return "Boom"
    else:
        print(n)
        
print(fizzbuzz(105))

    