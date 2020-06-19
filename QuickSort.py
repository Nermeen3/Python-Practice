from random import randint
def RandomGenerator(size):
    return [randint(0, 50) for x in range(size)]


# Quick Sort: its implemented by recursively picking a pivot (last element in the array)
# time complexity is O(n2) in worst case if the array is sorted since it will compare and check for every element
# average and best case is O(nlogn) and space complexoty is constant O(1)


def QuickSort2(array, pivotIndex):
    if len(array) <= 1:  return array
    lower, mid, larger = [], [], []
    for i in array:
        if i > array[pivotIndex]:
            larger.append(i)
        elif i == array[pivotIndex]:
            mid.append(i)
        else:
            lower.append(i)
    print(array, array[pivotIndex])
    return QuickSort2(lower, len(lower)-1, 0) + mid + QuickSort2(larger, len(larger)-1)


print('quick sorted array', QuickSort2(RandomGenerator(31), len(array)-1))

