#implement a map function
def map_function(array, function):
    new_array = []
    for i in array:
        new_array.append(function(i))

    #map functions are basically like for each functions in javascript
    #applies the function for each element in the array and returns a copy of that array

    return new_array

#implement a filter function
def filter_function(array, function):
    new_array = []
    for i in array:
        if function(i):
            new_array.append(i)

    #when the function returns true that value is copied into the returned array
    #other values which evaluate to false are filtered out

    return new_array

#implement a reduce function
def reduce_function(array, function):
    n = len(array)
    value = 0
    inital = array[0]
    for i in range(n-1):
        value = function(inital, array[i+1])
        inital = value

    #this iterable returns a single value
    #applies the function to the first element and the next element of the array and the result is stored
    #then function is applied to the result and the next element
    #this continues until the last element of the array is reached

    return value

#how to use the iterator in python?




#how to use the enumerator function in python?





#implement prime_helper function
'''given a number n, write a function which prints out all the primes
and returns the total number primes that are in this range'''

#def all_primes(n):
'''
>>> a = all_primes(5)
2
3
5
>>> a
3
'''

def prime_helper(n, check_prime):

    #if current is prime then increment number of primes
    #else if current is not prime then increment current
    #else if current is not prime or 
