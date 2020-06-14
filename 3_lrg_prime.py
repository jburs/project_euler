#jason Bursey, 2018-06-01
#
#largest prime factor of 600851475143
#
import math

def primes(n):
    primes=[]
    top=int(math.sqrt(n))
    for i in range(3,top+1,2):
        if n%i==0:
            x=i                       #get factor
            for j in range(3,x+1,2):
                if ((x%j==0) and (x==j)):
                    primes.append(x)
                elif (x%j==0):
                    break
    return primes

print (primes(600851475143))





