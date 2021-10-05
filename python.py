#using map + lambda
#using map + filter

#double for loop in a comprehension
# nums = [1, 2, 3, 4]
# count = 0
# new_list = [(i, j) for i in 'abcd' for j in range(len(nums))]
# print(new_list)

#dictionary comphrension
# names = ['seth', 'harry', 'mike']
# numbers = [707, 110, 404]
# dict = {k:v for k, v in zip(names, numbers)}

#set comprehension
# nums = [1, 1, 2, 3, 4, 4, 5, 6, 7, 6, 8, 9]
# new_set = {i for i in nums}
# print(new_set)

#how does this work?
#zip object combines two lists into pairs of tuples
#the first iterator goes through the first position and the second goes through the second in the first tuple for the first iteration
#using multiple iterators you have to go through multiple tuples
#either return a list or dicitonary/set with braces or curly brackets


#single tuple is not an iterable object




#how to create a 2-D array in python

# rows, cols = (9, 9)
# #method 1
# arr = [[0] * cols] * rows
#
# #method 2
# arr2 = []
# for i in range(rows):
#     col = []
#     for j in range(cols):
#         col.append(0)
#     arr2.append(col)
#
# #method 3
# arr3 = [[0 for i in range(cols)] for j in range(rows)]









#cube sum
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9


rows, cols = 9, 9
arr = [[0] * cols] * rows   #initialize the 2-D array

for i in range(rows):       #initalize the value of each row from 1 to 9
    for j in range(cols):
        arr[i][j] = j + 1

                            #sum a cube for each row
                            #try three sum with a sliding window

#SLIDING WINDOW: fixed and dynamic window

#max subarray of k size in an array

array = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]

def maxSumSubarray(array, window):
    maxValue = 0
    currentSum = 0

    n = len(array) - 1
    for i in range(n):
        currentSum += array[i]
        #sliding window
        if i >= window - 1:
            maxValue = max(maxValue, currentSum)
            currentSum -= array[i - (window - 1)] #drops the last value as the window moves forward

    return maxValue

#smallest subarray with a given sum

def smallestSubarray(array, targetSum):
    n = len(array) - 1
    start, end, currentSum, minValue = 0, 0, 0, n

    for i in range(n):
        currentSum += array[i]
        while currentSum >= targetSum:          #two pointer/dynamic window uses a while loop as well as a start and end pointer
            minValue = min(minValue, i - start + 1)
            currentSum -= array[start]
            start += 1

    return minValue
