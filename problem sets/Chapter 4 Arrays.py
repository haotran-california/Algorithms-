#even odd sorting function for arrays

# def even_odd(A):
#     next_even = null, next_odd = 0, len(A) - 1
#     while next_even < next_odd:
#         if A[next_even] % 2 == 0:
#             next_even += 1
#         else:
#             A[next_even], A[next_odd] = A[next_odd], A[next_even]
#             next_odd -= 1
#
# unsorted_array = list(1,5,2,3,8,4,3,2,7)
# for i in unsorted_array:
#     print(i)


#how to pass an array as an arguement
#how to declare an array with initalization list


#function to read letter into nato

# userinput = input("Please enter the letters your want to convert: ")
# string = ""
# letters = ['A','B','C']
# nato = ["Alpha","Bravo","Charlie"]
#
# for letter in userinput:
#         for item in range(0, len(letters)):
#             if letter.upper() == letters[item]:
#                 string += (nato[item] + " ")
#
# print(string)


#DUTCH FLAG PARTITION
# array = [0,1,2,3,2,0,1,3]
# def dutch_flag_partition(pivot_index, A):
#     pivot = A[pivot_index]
#     # First pass: group elernents smaller than pivot
#     for i in range(len(A)):
#         # Look fot a snaTTer el.ernent,
#         for j in range(i + 1, len(A)):
#             if A[j] < pivot:
#                 A[i], A[j] =  A[j], A[i]
#                 break
#
#
# dutch_flag_partition(2,array)
# print(array)


#
# def partition(arr, low, high):
#     i = (low-1)         # index of smaller element
#     pivot = arr[high]     # pivot
#
#     for j in range(low, high):
#
#         # If current element is smaller than or
#         # equal to pivot
#         if arr[j] <= pivot:
#
#             # increment index of smaller element
#             i = i+1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return (i+1)
#
# array = [0,1,2,3,2,0,1,3]


def even_odd (A) :
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else :
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return

array = [0,1,2]
print(even_odd(array))
