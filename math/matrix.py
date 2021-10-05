import numpy as np
from numpy.linalg import matrix_power

#add 2D array with another 2D array
a = np.array([ [1, 2, 3,], [4, 5, 6] ])
b = np.array([ [3, 2, 1], [6, 5, 4] ])

#print(a + b)
#print(b - a)

#np array object .shape returns (r, c)
# .size returns the product of r and c

#matrix class
m = np.matrix([ [1, 2, 3,], [4, 5, 6] ])
n = np.matrix([ [1, 2], [3, 4], [5, 6] ])

#print((m * n) * m)




#use linear algebra to solve for nth term of a recurence relation

#find the nth term of fibonnaci sequence
def nthTerm(n):

    f1, f2 = 1, 1
    inital_matrix = np.matrix([ [f1, f2] ])
    trans_matrix = np.matrix([ [0, 1], [1, 1] ])

    trans_matrix = matrix_power(trans_matrix, n)
    result = inital_matrix * trans_matrix
    print(result[0, 1])




def expMatrix(m, n):
    #initalize 2D array of shape m
    rows = len(m)
    cols = len(m[0])
    result = [[0] * cols] * rows

    #multiply matrix n times and store values in a list




    #organzie array of matrix values into matrix
    index = 0
    for r in range(rows):
        for c in range(cols):
            arr = multiply(m)
            result[r][c] = arr[index]
            index += 1


    print(result)

def multiply(m):
    rows = len(m)
    cols = len(m[0])

    arr = []
    value = 0
    for r in range(rows):
        for c in range(cols):
            if r == cols - 1 and c == rows - 1:
                arr.append(value)
                value = 0
            else:
                value += m[r][c] * m[c][r]
    return arr


m = [[0, 1], [1, 1]]
print(multiply(m))
