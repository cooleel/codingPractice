'''
looking for prime numbers
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
count_primes(100) --> 25
By convention, 0 and 1 are not prime.
'''

def count_primes(num):
    #check for 0 or 1
    if num <2:
        return 0
    #2 or greater
    #store our primes
    primes = [2]
    #counter going up the input num
    x = 3

    # x is going through every number up to input num
    while x <= num:
        #check if x is a prime number
        for y in primes:
            #check every even number
            if x%y ==0:
                x +=2
                break
        else:
            primes.append(x)
            x +=2
    print(primes)
    return len(primes)
