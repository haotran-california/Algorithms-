#SLIDING WINDOW: fixed and dynamic window

#max subarray of k size in an array
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

#using swaps
def rightRotation(arr, rotations):
    #left rotation with swap
    n = len(arr)
    #for each element swap it with the element to the left of it

    for i in range(rotations):
        for i in range(n-1):
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp

    #the space complexity is the space of the array
    #the time complexity is O(n), linear, the length of the array for 1 rotation
    #the time complexity for multiple rotations is exponetial for n ^ number of rotations

    return arr

#using two stacks
def rightRotation(arr):

    #using two stacks
    queue_1 = []
    queue_2 = []

    n = len(arr)
    for i in range(n):
        queue_1.append(arr[i])
        if i == n - 1:
            queue_2.append(arr[i])

    shifted_arr = []
    for i in range(n):
        if i == 0:
            shifted_arr.append(queue_2.pop(0))
        else:
            shifted_arr.append(queue_1.pop(0))
    #space complexity: queue_1 will always have n - 1 elements and queue_2 will have 1 element for O(n) space complexity
    #time complexity:O(2n) time complexity due to having two foor loops, simplifies to O(n), linear time
    return shifted_arr



def removeElement(arr, val):
    start = 0
    end = len(arr) - 1

    #why isn't my array popping the third
    # I can't rely on popping them by index because everytime I pop an element the length of the array changes
    while start <= end:
        if arr[start]  == val:
            arr.pop(start)
            print("start pop")
        if arr[end] == val:
            arr.pop(end)
            print("end pop")


        start += 1
        end -= 1
        continue
    print(start , end)
    return arr
#the constraints of this problem is modifying the input array in place

#looping through this problem once is O(n) time and space complexity
#however it is more efficent to use two pointers to loop throught half of the arrays
#this is like divide and conquer

arr = [0,1,2,2,3,0,4,2]




#fixed length window of 3
#peak is defined as a number larger than the one next to the left and right

def peakFinding(arr):

    peaks = []
    n = len(arr)
    window = 3

    #use a window from right to left
    for i in range(n):
        if i >= window - 1:
            #check for peak
            if arr[i-1] > arr[i-2] and arr[i-1] > arr[i]:
                peaks.append(arr[i-1])

    #use a window from left to right
    # for i in range(n - (window - 1)):
    #     if arr[i + 1] > arr[i + 2] and arr[i + 1] > arr[i]:
    #         peaks.append(arr[i+1])

    return peaks


def consecutiveOnes(arr):

    num = 0
    start = 0
    end = 0
    n = len(arr)

    while end != n or start != n:
        if arr[start] == 1:
            while arr[end] == 1:
                end += 1
            num = max(end - start, num)
            start = end
        else:
            start += 1




    return num


arr = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]





def numArray(arr):

    n = len(arr)

    for i in range(1, n + 1):
        #for the first iteration add 1 to the begining of the array
        if i == 1:
            arr[-i] = arr[-i] + 1

        if arr[-i] == 10:
            #when the index goes out of range then create a new array 1 bigger
            if i  + 1 > n:
                arr[-i] = 0
                arr.insert(0, 1)

            else:
                arr[-i] = 0
                arr[-i - 1] += 1

        else:
            continue

    return arr


#left rotation with modular
def l_Rotate(d, arr):

    #create a new array
    n = len(arr)
    new_arr = [0] * n

    for i in range(n):
        idx = ((n + i) - d) % n
        new_arr[idx] = arr[i]


    return new_arr

arr = [7, 8, 9, 10]


#left rotation with reversing arrays



#consecutive increasing integers of window sized k
def increasing(arr, k):
    n = len(arr)
    start = 0
    end = 1

    #is there a more simple way to loop through this array in an interval?
    for i in range(1, n - k + 1):
        #comparision between pointers
        if arr[end] > arr[start]:
            pass
        else:
            return print("false")

        #jump intervals with pointers
        if (i + 1) % k == 0:
            start += 2
            end += 2
        else:
            start += 1
            end += 1


    return print("true")





arr = [1, 2, 3, 7, 8, 9, 11, 12, 13]



#given an array of numbers find all subarrays which add to a given number

array = [1, 7, 4, 3, 1, 2, 1, 5, 1]

def subArraySum(arr, d):
    n = len(arr)
    start, end, sum = 0, 0, 0
    ans = []

    for i in range(n):
        #initalize the start and end index and sum
        #restarting count but one iteration forward
        start, end = i, i
        sum = 0

        #continue until the sum is less than or equal to target, d
        #do not continue end pointer if it will go out of boudns
        while sum <= d and end <= n - 1:
            sum += array[end]
            if sum == d:
                ans.append((start, end))

            end += 1


    return ans

def subArraySum_2(a, target):



    return 0


#kadane's algorithm
#navie approach
def maxSum(arr):
    n = len(arr)
    fast = 0
    m = 0
    sum = 0

    for i in range(n):
        sum = 0
        fast = 0
        while end <= n - 1:
            sum += arr[fast]
            m = max(sum, m)
            fast += 1
    return m

arr = [-2, -3, 4, -1, -2, 1, 5, -3]

def kadane(arr):

    #find the positive numbers
    n = len(arr)
    pos = []
    for i in range(n):
        if arr[i] >= 0:
            pos.append(i)

    index = 0
    sum = 0
    for i in range(n):
        
        if arr[i] = pos[index]
        index += 1
