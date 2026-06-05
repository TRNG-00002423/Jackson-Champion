

#result = []
#for i in range(len(a)):
#    result.append(a[i]+b[i])

#print(result)

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)

arr= np.array([[1,2,3], #2D Array
               [4,5,6]])

print(arr)

arr1 = np.array([1,2,3,4])
print(arr1 * 2) #Apply *2 to all elements
print("*" * 20) 
print(np.square(arr1)) #Square each index
print("-" * 20)

arr2 = np.array([1,4,9,16])
print(np.sqrt(arr2)) #find square root
print(np.sum(arr2)) #Find sum

arr3 = np.array([3,4,5,6,2,10,12,33,2,7,12])
print(np.min(arr3)) #Find minimum
print(np.max(arr3)) #Find maximum

print(np.zeros((2,3))) #initialize 2x3 matrix of 0s

print(np.ndim(arr3)) # Gives dimensions

print(np.shape(arr3))