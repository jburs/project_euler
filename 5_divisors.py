# Euler problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#

found = False
number = 20
divisors = [i for i in range(1,21)]


while found != True:
    #create empty list to store even divisors
    results = []

    #check each divisor against current number
    for divisor in divisors:
        if number%divisor == 0:
            results.append(divisor)
    
    #check if every divisor divided eavenly
    if len(results) == len(divisors):
        found = True
        print(number)
    else:
        #only check numbers divisible by 20
        number += 20





