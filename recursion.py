from functools import lru_cache

#@Lru_cache(maxsize = 1000)
def fib(n, arr):


    if n <= 2:
        return 1
    else:
        arr.insert(0,n-1 + n-2)
        return fib(n-1, arr) + fib(n-2, arr)
                                                                  #how to use memoization to reduce space/time complexity
                                                                  #what is the complexity currnetly?                                                                  #the arrays in python are passed by refference to the function
cache = {}
def fib_2(n):

    if n in cache:
        return cache[n]

    if n <= 2:
        value = 1

    else:
        value = fib_2(n-1) + fib_2(n-2)

    cache[n] = value
    return value



arr = []
def factorTree(n):

    if n == 1:
        return
    else:
        value = factorTree(n/2) if n % 2 == 0 else factorTree(n/3)
        arr.append(value)
        return value


a = int(3) / int(2)
b = 3 // 2

#number of paths from starting square to ending square in a matrix

def numPaths(rows, cols):

    return 0


def numPartitions(n, m):

    return 0
