def generateAlpha():



    return 0



def countdown(start):

    while start >= 0:

        yield start
        start = start -1

for i in countdown(10):
    print(i)
