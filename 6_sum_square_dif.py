# Euler problem 6
# Sum square difference
# The sum of the squares of the first ten natural numbers is, 12+22+...+102=385
# The square of the sum of the first ten natural numbers is, (1+2+...+10)2=552=3025
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_square_dif(n):
	return sum(n)** 2- sum([i** 2 for i in n])

print(sum_square_dif(range(1,101)))

