# 
#
# sum of even-valued fibonaccie numbers less than 4 million
#
fib1,fib2,fib3=1,2,3
sum=0

while (fib3 < 4000000):
    fib3=fib1+fib2
    fib1=fib2
    fib2=fib3
    if (fib3 < 4000000) and (fib3%2==0):
        sum+=fib3

print (sum)

