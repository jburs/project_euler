# Euler problem 9: special triangle triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
#


# through calculus: a = (2,000b-1,000,000)/(2b-2,000)
#                   c = 1,000-b-a
b=2
while b < 499:
    a = (2000*b-1000000)/(2*b-2000)
    c = (1000-b-a)
    if int(a)+int(b)+int(c) == 1000 and a*a+b*b == c*c:
        print(a, b, c)
        print( a * b * c)
    
    b += 1


