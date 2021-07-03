from numpy import *
from numpy import concatenate

arr1 = array([1,2,3,4,5])
print(arr1)
print()
i = 1
while i == 1:
    print(arr1 + 5)
    i+=1
print()
for e in range(1):
    print(arr1 + 5)
print()
arr3= arr1 + 5
print(arr3)
arr2 = array([1,4,7,8,9])
print(arr2)
print()
arr4 = arr1 + arr2
print(arr4)
print()
print(sum(arr2))
print()
print(sum(arr1))
print()
print(min(arr1))
print()
print(min(arr2))
print()
print(max(arr1))
print()
print(max(arr2))
print()
print(concatenate([arr1,arr2]))
arr2 = arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
arr2 = arr1.view()
print()
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
arr2 = arr1.copy()
print()
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
arr1[1] = 7
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))