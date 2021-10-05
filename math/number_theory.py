#recursive formula for LCM
import math

def LCM(a, b):
    #iterative solution

    #generate a list of multiples from the original value to the value of a x b
    #therefore the value of the LCM must be in this array
    list_a = [i * a for i in range(1, a)]
    list_b = [i * b for i in range(1, a)]

    #find the lowest matching value in both arrays
    #brute force with nested loops
    low = a * b
    for i in list_a:
        for j in list_b:
            if i == j:
                low = min(low, i)

    #space complexity is 2 * [a * b]
    #time complexity is O(n^2) because searching for lowest value is done in that runtime
    return low




#recursive formula for GCD
def GCD(a, b):
    #a is the larger number and b is the smaller number

    if a % b == 0:
        #why is my return statement here returning a none value
        return b
    else:

        return GCD(b, a % b) #because I forgot to stay return here
        #whenever you call a recursive function you need to call it with return
        #otherwise the value will not get stored

def test(a):

    c = 0
    while a / 2 != 1:
        c += 1
        a = a / 2

    return c

def DecimalToBinary(num):

    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

DecimalToBinary(12121212)

0101110001111010001111100

#generate primefacotrization
def all_primes(n):

    prime = 2 #set prime to the first prime number
    count = 0
    while n != 1: #condition accounts for the case where n / prime is equal to 1
        if n % prime == 0:
            n = n / prime
            count += 1
            print(prime)
        else:
            prime += 1 #since the divisiblity of lower numbers are acounted for than n % prime == 0 will always be a prime number

    return 'the number of prime numbers is {}'.format(count)



def prime_helper():



    return 0


def primeCheck(n):

    sqrt = math.sqrt(n)
    for i in range(2, math.ceil(sqrt) + 1): # +1 guards against the edgecase, boundary case
        if n % i == 0:
            return False

#used recursion and higher order function to check prime
def is_prime(n):

    prime = 2
    def helper(prime):
        if n == 2 or prime >= 11:
            return True
        if n % prime == 0 and prime < n:
            return False
        else:
            return helper(prime + 1)
        return True

    return helper(prime)





#recursive formula for binomial coefficient
def binomialCoefficient(n):

    return 0




#generate the divisors of a number n
def generateDivisors(n):

    a = range(1, (n+1))
    results = []

    for i in a:
        if n % i == 0:
            results.append(i)
        else:
            continue

    return results




#filter prime numbers using a seieve
def seivePrimes(end):

    #populate array from start to end
    primes = []
    for i in range(2, end):
        primes.append(i)

    #use seieve to filter out non-primes
    #from inital current 1 to current 7, remove all multiples of current
    #the resulting array is all prime

    current = primes[0]
    while current != 11:
        for i in primes:
            if i % current == 0 and i != current:
                primes.remove(i)
        current += 1

    #what is the runtime?
    #not as fast as O(NLog(N)) but not as slow as O(n^2)

    #there is 4 iterations to the for loop
    #iteration of 2 cuts it in 1/2
    #iteration of 3 cuts it in 1/5
    #iteration of 5 cuts it in aprox 1/12
    #iteration of 7 cuts in in appox 1/100

    #O(2N) therefore this is O(N)

    return primes


#generate prime numbers using a generator
def millsGenerator():
    mu = 1.3063378838630806904686144926
    n = 0

    while n != 8:
        yield math.floor(mu ** 3 ** n)
        n += 1


def generatePrimeNum():

    return 0




def fastExponation(n, k):
    #where n is the number and k is the power to which it is raised
    #divide and conquer algorithm
    #cache required to reduce number of calls

    cache = {}

    #basecase
    if k == 1:
        return n
    else:
    #recursive case
        if k % 2 == 0:
            if k in cache:
                c = cache[k]
            else:
                c = fastExponation(n, k / 2)
                cache.update({k: c})
                print("evens ", cache)
            return fastExponation(n, k / 2) * c
        else:
            if k in cache:
                c = cache[k]
            else:
                c = fastExponation(n, k // 2)
                cache.update({k: c})
                print("odds ", cache)
            return fastExponation(n, k // 2 + 1) * c

            #there are two return statements and four recursive calls
            #lines 169 and 171 return the product of two recursive calls
            #the call stack works in such a way so that the value of the last call is returned first and the first call is returned lat
            #the value of the last returned call is the value which is the result of the function

#unit digit sum
#enter numbers until q, quit
#find the unit digit sum of those characters

def unitDigitSum():



    return 0


#next divisible number
def nextDivisibleNumber(n, a):

    return n + a - (n % a)


#last divisible number
def lastDivisbleNumber(n, a):

    return n - (n % a)



#large number multiplication
def largeMultiplication(a, b):
    result = 0

    #convert a and b into binary
    binary_a = a
    binary_b = b

    #use binary multiplication

    return result
