### BUBBLE SORT: its a sorting algorithm that runs through the array one time
### to check if the array is sorted O(n) and if not sorted gets in the second
### loop to swap elements by comparing every two elements together
### time complexity for this search is O(n2) and O(n) for an already sorted array
### the name "bubble" reason: because in each iteration the largest numbers "largest bubbles" make their way to the end of the array "top"



def bubbleSort(array):
    array = [5,1,4,2,8]
    print("starters array: ", array)
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            for j in range(0, len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                #print(array)

array = [4,6,8,0,9,7,5,3,5]
bubbleSort(array)
