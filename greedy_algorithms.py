
import math
#eygptian sum
def eygptian_sum(n, d):

    if d < n: #base case
        return 0
    else:
        frac_input = n / d
        next_sum = math.ceil(d / n)
        print( 1 / next_sum)


def scheduling(n):
    #sort activities based on finishing time
    sorted_pairs = sorted(zip(end, start), reverse = True) #sorts start
    tuples = zip(*sorted_pairs)
    sorted_end, sorted_start = [list(tuple) for tuple in tuples]

    #iterate backwards through starting times
    count = 0
    for i in range(len(sorted_start) - 1, 0, -1):
        if sorted_end[i] <= sorted_start[i]:
            count += 1

    return count



#create a 2D boolean array

boolean_arr = []
for i in range(11):
    for j in range(11):
        new_arr = []
        boolean_arr[j] = new_arr

print(boolean_arr)
