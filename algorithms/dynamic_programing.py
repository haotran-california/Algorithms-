
#01 knapsack problem

#navie solution, brute-force, exhaustive search 
def KS(n, C, w, v):
    if n == 0 or C == 0:
        result = 0
    elif w[n] > C:
        result = KS(n-1, C, w, v)
    else:
        temp1 = KS(n-1, C, w, v) # don't choose the first item
        temp2 = v[n] + KS(n-1, C - w[n], w, v) #choose the first item
        result = max(temp1, temp2)

    return result


w = [0, 1, 2, 4, 2, 5] #weight of each item
v = [0, 5, 3, 5, 3, 2] #value of each item
n = len(w) - 1
capacity = 10

print(KS(n, capacity, w, v))
