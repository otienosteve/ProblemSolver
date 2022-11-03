import itertools
from functools import reduce

def smallSum(arr):
 arr2=[0]

 for size in range(2, len(arr) + 1):
  
   for subset in itertools.combinations(arr, size):
       arr2.append(reduce(lambda a,b: a+b, subset))
 arr2.extend(arr)
 for i in range(len(arr2)+1):
    if i not in arr2:
        return i

print(smallSum([1,2,5]))
print(smallSum([5,  7,  1, 1,  2,  3,  22]))