import math


#DAY 1
def fizzBuzz(n):
    #initalize a list and a string
    list = []
    result = ""

    #create a list from (1-n)
    for i in range(0,n):
        list.append(i + 1)

    #check each element in the list
    for i in list:
        if i % 3 == 0:
            result = result +  "Fizz"
        if i % 5 == 0:
            result = result + "Buzz"
        if result != "":
            print(result)
            result = ""
        else:
            print(i)

def compareTriplets(a,b):

    #initalize array and values for element 0 and 1
    comp_score = []
    a_score, b_score = 0, 0

    #compare each element in a and b against eachother
    n = len(a)
    for i in range(0, n):
        if a[i] > b[i]:
            a_score += 1
        elif a[i] < b[i]:
            b_score += 1
        else:
            continue

    #add scores to array
    comp_score.append(a_score)
    comp_score.append(b_score)
    return comp_score

def countApplesAndOranges(s, t, a, b, apples, oranges):

    #initalize values
    apples_in_range = 0
    oranges_in_range = 0

    for i in apples:
        if (i + a) >= s and (i + a) <= t:
            apples_in_range += 1

    for j in oranges:
        if (j + b) >= s and (j + b) <= t:
            oranges_in_range += 1

    print(apples_in_range)
    print(oranges_in_range)

def camelcase(s):

    #init
    num_words = 0
    #find all capital letters in string
    capital = []
    for letter in s:
        if letter.isupper():
            capital.append(letter)

    #convert captial letters to indices
    index = []
    for i in capital:
        element = s.index(i)
        index.append(element)


    num_words = len(index) + 1
    return num_words

def index(V, arr):

    count = 0
    for i in arr:
        count += 1
        if i == V:
            break


    return count - 1;

def insertionSort1(n, arr):

    pivot = arr[n]
    for i in reversed(range(len(arr) - 1)):
         print(arr)
         if arr[i] > arr[i-1]:
             arr[i] = arr[i-1]
         else:
             arr[i] = pivot
             break




    return arr

# arr = [1,2,3,4,5,3]
# print(insertionSort1(5, arr))

#DAY 2

def diagonalDifference(arr):
    difference = 0
    sum_l_diagonal = 0
    sum_r_diagonal = 0

    for i in range(n):
        for j in range(n):
            if j == i:
                sum_l_diagonal += arr[i][j]
            if j == (n - 1) - i:
                sum_r_diagonal += arr[i][j]

    difference = abs(sum_l_diagonal - sum_r_diagonal)

    return difference

def average(array):
    average = 0

    return average




fizzBuzz(15)
