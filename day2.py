"""
Day 2: Variables and Data Types
- Topics:
- Learn about variables and different data types: int, str, float, bool.
- Type casting: converting between types.
Project:
    Create a program that takes user input for their name and age,
    then prints a greeting with their name and calculates the year they were born.
"""

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
year_born = str(2025 - age)
print(f'Greetings {name}, you were born in  the year {year_born}.')