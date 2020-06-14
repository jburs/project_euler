# Euler project challenge 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#

largest_palindrome = []

#iterate through all products
for i in range(100,999,1):
    for j in range(100,999,1):

        #convert to list, iterate [::-1] for reverse
        number = i*j
        forward = [int(x) for x in str(number)]
        backward = forward[::-1]

        #store unique palindromes
        if forward == backward and number not in largest_palindrome:
            largest_palindrome.append(number)

# sort smallest to largest
largest_palindrome.sort()

#print final value in list, the largest palindrome
print(largest_palindrome[-1])
