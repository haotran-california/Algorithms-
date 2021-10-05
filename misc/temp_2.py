contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
# [ [8, 1], [5, 1], [2, 1], [1, 1], [10, 0], [5, 0] ]
#sort the cols in rows but sort the rows by the 2nd element

#convert 2D array into an array of tupples
c = [(i[0], i[1]) for i in contests]

#sort the array of tuples
#sort by the max importance
#implement merge sort on the list of tupples





#proper way

# char = 'a'
# alphabet = []
# for i in range(0, 26):
#     alphabet.append(char)
#     char = str( (ord(char) + 1) )
#
# print(alphabet)

import string

alphabet = list(string.ascii_lowercase)

string_arr = ["strog", "bloh"]



a = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]

rows = len(a)
cols = len(a[0])

c_array = []


for c in range(cols):
    for r in range(rows):
        c_array.append(a[r][c])

print(c_array)
