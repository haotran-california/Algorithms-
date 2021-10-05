def solution(data, n):

    #return none based on constraints
    if n == 0:
        return

    elif len(data) > 100:
        return

    # #create a histogram to map the frequency of each element/task
    hist = dict()
    for i in data:
        hist[i] = hist.get(i, 0) + 1

    #append every task that occurs more than n times in a list
    remove_tasks = [i for i in data if hist[i] > n]

    #remove tasks from data
    for i in remove_tasks:
        data.remove(i)

    return data


    #how to only loop through data once instead of twice
    #how to use set, filter, lambda, or list comprehension to lower time complexity
    #
    # solution = [i for i in data if data.count(i) <= n]
    # return solution
    #time complexity of this is linear, O(n)





data = [1, 2, 2, 3, 3, 4, 5, 5]
n = 2

print(solution(data, n))
