# Euler problem 12: higly divisible triangular number
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?


# Method: Trial division - test numbers from 1 to square root of number
import math


found = False
num = 1
count = 1
while found == False:
    factors = []
    for i in range(1, math.floor(math.sqrt(num+1))):
        if num%i==0:
            factors.append(i)
            factors.append((num/i))

    if len(factors) > 500:
        found = True
        break

    count += 1
    num += count

print(f"num: {num} ,factor length: {len(factors)}")
print(factors)
