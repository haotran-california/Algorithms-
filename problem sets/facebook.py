
def almostSubstring(t, s):
    n1 = len(t)
    n2 = len(s)
    fast, slow = 0, 0
    n = 0

    while(slow < n1 - (2 * n2 - 2)):
        #iterate through the string by length of s by step of 2
        text = ""
        fast = slow
        for i in range(n2):
            text += t[fast]
            fast += 2
        print(text)
        if text == s:
            n += 1

        slow += 1

    return n

    #number of possible times to iterate over the string
    #use two pointers start and end


#almostSubstring("azcabcab", "acb")



def sumOfFirstNumbers(numbers):
    n = len(numbers)
    a = 0
    start = 0
    repeat = True

    while(repeat):

        #find the first non zero element of the array
        for i in range(start, n):
            if numbers[i] > 0:
                x = numbers[i]
            else:
                continue

        #remove x in each index
        for i in range(start, n):
            if numbers[i] >= x:
                numbers[i] -= x
            else:
                break
        a += 1
        start += 1

        #check to see if all the elements in the array is zero
        if max(numbers) == 0 and min(numbers) == 0:
            repeat = False


    return a

numbers = [3, 3, 5, 2, 3]
print(sumOfFirstNumbers(numbers))
