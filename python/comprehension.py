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

print(arr)
#sum a cube for each row
def cubeSum(arr):

    len_row = len(arr)
    len_col = len_row
    list = []

    for row in range(len_row - 2):
        for col in range(len_col - 2):
            sum += arr[row][col]
            sum += arr[row][col + 1]
            sum += arr[row][col + 2]
            sum += arr[row + 1][col]
            sum += arr[row + 1][col + 1]
            sum += arr[row + 1][col + 2]
            sum += arr[row + 2][col]
            sum += arr[row + 2][col + 1]
            sum += arr[row + 2][col + 2]
            list.append(sum)
            sum = 0
            #reset sum after every iteration of the inner for loop because the inner for loop will go 7 times before exiting to the outter for loop

    #the space complexity is that of the 2D array
    #the time complexity is O(n^2)
    return max(list)

#try three sum with a sliding window
