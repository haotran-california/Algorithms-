

#generate all possible permuations of a set
#generate all possible permuations of the string


#generate all possible permutations of the string using decision space and subset
def permutations(str_arr):
    subset = []
    decision_space = []
    for i in str_arr:
        decision_space.append(i)

    return helper(array, subset, decision_space)

def helper(str_arr, subset, decision_space):
    if len(subset) == len(str_arr): #base case
        print(subset)
    else:
        #remove from decision space the elements in the subset
        for i in subset:
            for j in decision_space:
                if i == j:
                    decision_space.remove(i)

        n = len(decision_space)
        for i in range(n): #number of inital branches
            #add each element in the decision space into the next part of the subset
            new_element = decision_space[i]
            subset.append(new_element)
            return helper(str_arr, subset, decision_space)




#generate all possible permutations using swaps
def permutate_str(array, start, end):
    c = 0
    if start == end:
        print(array)
    else:
        for i in range(start, end + 1): #why is it start end + 1 here?
            c += 1
            print(c)
            array[start], array[i] = array[i], array[start] #swap occurs instaneously
            permutate_str(array, start + 1, end) #why do we not return the value of recursion?
            array[start], array[i] = array[i], array[start] #by reseting the inital condition backtracking occurs as other condition are iterated through

            #use one recursive call with a for loop to iterate through multiple recursive calls

    #range from start will ensure that start and i cannot swap with values before start, only the current start values and next values
    #^^this helps to correctly iterate throught the possiblities
    #range end has to do with going down the rest of the tree branches
    #return will only return one value whereas the recursive call will backtrack through all possibities

    #what time complexity is this algorithm?
    #estimating from how fast it runs it can be polynomial time, linear logarithmic, logarithmic,
    #it likely isn't faster than polynomial time
    #count the number of possiblities from the back track



array = ["A", "B", "C"]
permutate_str(array, 0, len(array) - 1)
