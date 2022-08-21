'''Write a Python function to calculate the factorial of a number (a non-negative integer). 
The function accepts the number as an argument.'''

#  n! = n * (n-1) * (n-2) * (n-3)..... * 1 = n * factorial (n-1)
from math import factorial

def factorial_func(n):
    if n==0:
        return 1
    else:
        return n * factorial (n-1)
print(factorial_func(5))