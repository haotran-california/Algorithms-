
#ATTEMPT 1: BUBBLE SORT
array = [1,41,35,23,1,5,34,23]
def bubblesort(Array):
    index = 0
    while index != len(Array) - 1:
        print("sort#", index)
        if Array[index] > Array[index+1]:
            Array[index], Array[index+1] = Array[index+1], Array[index]
            index += 1
        else:
            index += 1


#TIME COMPLEXITY OF O(n-1)


# GEEKS FOR GEEKS CODE
# array = [1,41,35,23,1,5,34,23]
# print("unsorted array: ", array)
#
# def bubblesort(array):
#     n = len(array)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if array[j] > array[j+1]:
#                 array[j],array[j+1] = array[j+1], array[j]
#
# bubblesort(array)
# print("sorted array", array)
#time complexity 0(n^2) or 0(n^n)

#ATTEMPT #1: SELECT SORT
array = [1,41,35,23,1,5,34,23]


def selectsort(array):
    n = len(array)-1
    min_value, min_index = array[0], 0
    for i in range(n-1):

        for i in range(n-1):
            if array[i] < min_value:
                min_value = array[i]
                min_index = i

        array[i] = min_value





#BINARY SEARCH
arr = [1, 2, 3, 4, 5, 6, 7, 8]

def binarySearch(arr, target):
    n = len(arr)
    index = 0

    while arr[index] != target:
        n = n // 2
        if target > arr[index]:
            index += n
        else:
            index -= n

        if arr[index] == target:
            return index

    return -1





#binary search using three pointers
def binarySearch_(arr, x):

    low, high, mid = 0, len(arr) - 1, 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return - 1

#binary search using recursion
def BinarySearch(arr, x):
    h = len(arr)
    m = h // 2

    if arr[m] == x:
        return m
    elif arr[m] > x:
        #return the top half
        arr = arr[m:h]
        return BinarySearch(arr, x)
    elif arr[m] < x:
        #return the bottom half
        arr = arr[0:m]
        return BinarySearch(arr, x)
    else:
        return 0


arr2 = [1, 2, 3, 4]
#print(arr2[2:4])
BinarySearch(arr2, 2)
