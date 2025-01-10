"""
Day 5: Functions
Topics:
 - Learn how to define functions using def.
 - Understand function arguments, return values, and scope.
Project:
- Write a function that takes a number as input and returns the factorial of that number.
"""

def factorial_num(x):
    if x < 0:
        return "Please enter a positive number"
    result = 1
    for i in range(1, x + 1 ):
         result = result * i
    return result
    
numb = int(input("Please enter a positive integer: "))
print(f'The factorial of {numb} is {factorial_num(numb)}')