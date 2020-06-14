# Euler problem 10: Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
#

import math

primes = [2, 3, 5, 7]
num = 9

# get all primes below 2 million
while primes[-1] < 2000000:
    #assume num is prime
    prime = True

    # Test vs off numbers 3 to sqrt(num) + 1
    for i in range(3, math.ceil(math.sqrt(num))+1, 2):
        if num%i == 0:
            prime = False
        
    if prime == True:

        primes.append(num)

    num += 2

print(primes)

#sum all primes, excluding the final prime as it will be over 2 mil b.c while condition
print( sum(primes[:-1]))