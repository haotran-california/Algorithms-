
#create a dictionary from two parallel arrays

keys = ['red', 'green', 'blue']
values = [120, 255, 205]

#list comprehension
dict = { k:v for k, v in zip(keys, values)}

#zip puts together the first arguement with the second arguement for each of the two iterables
#zip returns the pair of values in a tuple
#call list on the zip object to convert into list for printing



print(list(zip(keys, values)))
