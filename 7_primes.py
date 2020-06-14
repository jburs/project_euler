# Euler problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
#

import math

primes = [2, 3, 5, 7]
num = 9

while len(primes) < 10001:
    #assume num is prime
    prime = True

    # Test vs off numbers 3 to sqrt(num) + 1
    for i in range(3, math.ceil(math.sqrt(num))+1, 2):
        if num%i == 0:
            prime = False
        
    if prime == True:

        primes.append(num)

    num += 2

print(primes[-1])






