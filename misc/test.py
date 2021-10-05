def LeastCommonMultiple(a, b):
    #euclidan method
    # ab = GCD(a, b) * LCM(a, b)

    #applying communicative property of multiplication
    # ab * 1/GCD(a, b) = LCM(a, b)
    # (a / GCD(a, b)) * b = LCM(a, b)
    # (b / GCD(a, b)) * a = LCM(a, b)

    #prime factorization method
    #generate primes factors and add to a list
    prime = 2
    list_a = []
    while a / prime != 1:   #can I factorize both a and b in the same loop?
        if a % prime == 0:
            a = a / prime
            list_a.append(a)
        else:
            prime += 1
    list_a.append(prime)    #how can I write this so that this line is not needed

    list_b = []
    prime = 2
    while b / prime != 1:
        if b % prime == 0:
            b = b / prime
            list_b.append(prime)
        else:
            prime += 1
    list_b.append(prime)

    #convert the two lists into histograms
    dict_a = {}
    for i in list_a:
        dict_a[i] = dict_a.get(i, 0)

    dict_b = {}
    for j in list_b:
        dict_b[j] = dict_b.get(j, 0)

    #compare the two dictionaries and store results in a list
    results = []

    key_a = dict_a.keys()
    key_b = dict_b.keys()
    print(key_a, key_b)

    for i in key_a:
        if dict_a[i] == 0:
            results.append(i)






    #compare list of two prime factors
    #add to list if the number is unqiue, if the number is not then add the number of multiples which are highest
    #prime factorizations sorts numbers from least to greatest
    #take the count of a the elements inside the list





    print(dict_a, dict_b)

LeastCommonMultiple(10, 15)
