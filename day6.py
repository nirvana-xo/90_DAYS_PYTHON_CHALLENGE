"""
Day 6: Lists and Tuples
Topics:
 - Learn about lists and tuples: how to create, access, modify, and delete elements.
 - List methods: append(), remove(), pop().
Project:
 - Create a program that takes a list of numbers and prints the sum and average.
"""

numbers_list = list(map(int, input("Please enter 5 numbers separated by commas: ").split(',')))
print("You entered:", numbers_list)
sum_of_list = sum((numbers_list))
avg_numbers = sum_of_list / len(numbers_list)
print(f'The sum of numbers in entered is: {sum_of_list} and its average is {avg_numbers}')