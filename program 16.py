# A program to print the exact square root numbers from 1 to given input number
# Input: 50
# Output:
#	1 4 9 16 25 36 49



# Code:

from math import sqrt,floor
n = int(input())
limit = floor(sqrt(n))
for i in range(1,limit+1):
    print(i*i)
