# Map : map() applies a function to every element of an iterable

numbers = [1,2,3,4,5]
double = list(map(lambda x:x*2, numbers))
print(double)

names = ["Oscar", "Audy", "Curtis", "Anuha"]
#Capitalize each name


#filter() - filters based on a predicate function or condition
numbers = [1,2,3,4,5,6,7,8,9,10]

squares = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 != 0, numbers ))

#reduce() - often as an aggegrator
from functools import reduce

numbers = [1,2,3,4,5]
total = reduce(lambda a, x:a+x, numbers)

# zip() : takes 2 or more iterables and combines element by element
# in tuples
names = ["Ken", "Natalie", "Thomas"]
grade = [85, 92, 84]
zip_name_grade = zip(names,grade)

list_name_grade = list(zip_name_grade)
print(list_name_grade)