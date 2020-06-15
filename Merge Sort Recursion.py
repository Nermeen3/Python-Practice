### Merge sort: works by dividing the array into halves and each half into another half
### until we're left with n arrays each holds one element from the original array
### then we go back up by comparing arrays and sorrting them as we go up
### time complexity is O(nlogn)
### Auxillary space is O(n)

from random import randint
def RandomGenerator(size):
    return [randint(0, 50) for x in range(size)]

def Merge(array1, array2):
    #print(array1, array2)
    newArray = []
    index1,  index2 = 0, 0
    for i in range(len(array1)+len(array2)):
        if index1 == len(array1):
            newArray.extend(array2[index2:])
            break
        elif index2 == len(array2):
            newArray.extend(array1[index1:])
            break
        elif array1[index1] < array2[index2]:
            newArray.append(array1[index1])
            index1+= 1
        else:
            newArray.append(array2[index2])
            index2+= 1
    #print(len(array1)+len(array2), len(newArray))
    #print('merged array: ', newArray)
    return newArray

def MergeSort(array):
    # Base Case when we reach last step of dividing the original array's elements
    if len(array) <= 1: return array
    # next is recusiveley divide the array into halves
    LArray, RArray = MergeSort(array[:int(len(array)/2)]), MergeSort(array[int(len(array)/2):])
    #print(LArray, RArray)
    return Merge(LArray, RArray)

print(MergeSort(RandomGenerator(14)))
