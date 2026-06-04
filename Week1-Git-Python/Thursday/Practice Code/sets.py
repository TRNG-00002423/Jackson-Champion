ids = {1,2,3,4,5}
empty_set = set() #Create an Empty Set

numbers={1,2,2,3,4,5,3} #Print 1 2 3 4 5 (Duplicates are removed
from_list = set([10,20,20,30]) #Creating a set from a list

ids = {1,2,3}
ids.add(4) #add 4 to set
ids.add(2) #won't add 2 since already exists

ids.remove(1) #removes 1
ids.remove(100) #error

ids.discard(2)
ids.discard(100) #not throw an error

val = ids.pop() #rempves arbitrary number

ids.clear() #Removes all elements

fruits = {"apple", "banana", "mango"}
vegetable = {"cabbage", "carrot", "lettuce"}

fruits_and_vegs = fruits.union(vegetable) #combines sets

#intersection elements contain in both sets
