def reverseString(string):

    start = 0
    end = len(string) - 1

    while start <= end:
        temp = string[start]
        string[start] = string[end]
        string[end] = temp

        start += 1
        end += -1

    return string

def palindrome(string):

    #read string into an array to avoid item assigment
    str_arr = []
    for i in string:
        str_arr.append(i)

    start = 0
    end = len(string) - 1

    while start <= end:
        if str_arr[start] != str_arr[end]:
            return print("this is not a palindrome")
        else:
            start += 1
            end += -1
            continue

    return print("this is a palindrome")

def longestSubString(string):
    str_arr = []
    for i in string:
        str_arr.append(i)

    start = 0
    runner = 0
    max_length = []
    n = len(str_arr)


    while start < n:
        length = 1
        cache = [str_arr[start]]
        while runner < n:
            if str_arr[runner] not in cache:
                length += 1
                cache.append(str_arr[runner])
            else:
                max_length.append(length)
            runner += 1
        start += 1

    return max(max_length)

def consecutiveNums(num):

    #the mistake I made was return the total number of consecutive 1's instead of the greatest consequtive 1's
    #split the array of binary number into separate arrays then record the length of the longest array
    return 0


#what is item assignment?





#2nd largest element
import random
b = []
for i in range(100):
    b.append(random.randint(0, 100))

#why is this algorithm wrong? 
def secondLargest(a):

    n = len(a)
    big = 0
    bigger = a[0]

    for i in range(n):
        if a[i] > bigger:
            big = max(big, bigger)
        bigger = max(bigger, a[i])

    return big

print(secondLargest(b))
print(sorted(b))
