tests = []

tests = ["login", "search", "checkout"]
mixed_list = [1, "login", True, "search","checkout"]

print(tests[0]) # Print First element "login"
print(tests[1]) # Print Last element "search"
print(tests[-1]) # Prints last element

tests[1] = "advance search" #Modify the list at element 2
tests.append("logout") # adds an element to end of list
tests.insert(0, "open page") #Adds at specified element
print(tests)
tests.remove("login") #Removes specific string
removed = tests.pop() #Returns and Removes last item or based on indexes

del tests[0] #removes element

"some value" in tests #True or False

tests.index("checkout") #returns index. Stops at the first

tests.count("login") #Count how many times it appears

tests.sort

tests.sort(reverse=True) #Sort descending

tests.reverse() #Sort Ascending

numbers = [1,2,3,4,5,6]
print(numbers[1:4]) #Slicing Prints element 1 up to 4 (not including last parameter)

numbers[:4] #start from beginning up to 4
numbers[3:] #Start at third index up to end