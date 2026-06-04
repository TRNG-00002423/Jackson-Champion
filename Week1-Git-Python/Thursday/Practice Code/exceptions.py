try:
    
    result = int(input("Enter a Number : "))

except ValueError as e:
    print(f"That is not a number --{e}")
    raise ZeroDivisionError("Some Text")
except (TypeError, KeyError) as e:
    print({e})
else:
    print("No Exception")
finally:
    print("clean up code")