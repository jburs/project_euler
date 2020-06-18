#  The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#   starting with 13, we generate the following sequence:
#  13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

import matplotlib.pyplot as plt

longest_chain = []
longest_num = 0

#loop through all numbers for testing. note num has to be odd to get 3*num+1 boost
for num in range(999999, 10000, -2):
    starting_num = num
    chain = []

    #apply positive and negative conditions to produce collatz chain    
    while num > 1:
        chain.append(num)
        if num%2 == 0:
            num = num/2
        else:
            num = 3*num + 1

    #chech if collatz chain is completed, test chain vs current leader
    if len(chain) > len(longest_chain):
        longest_chain = chain
        longest_num = starting_num


print(f"winning number: {longest_num}")
print(f"longest chain: \n{longest_chain}")

plt.plot(longest_chain)
plt.show()