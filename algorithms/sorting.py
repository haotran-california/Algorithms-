#radix/bucket sort

#bubble sort
#other sort

#insertion sort
def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        insert = arr[i]
        p = i - 1

        while insert < arr[p] and p >= 0:
            arr[p + 1] = arr[p]
            p -= 1

        arr[p + 1] = insert
        print(*arr)

#practice for counting sort
arr = [2, 3, 2, 1, 1, 0, 2, 1, 3]

#1. count the frequencies
#2. initalize an array of the same size
#find the of the elements within the array 

freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1

new_arr = [0] * len(arr)
