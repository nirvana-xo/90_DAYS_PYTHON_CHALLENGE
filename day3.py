"""
    Day 3: Conditional Statements
    Topics:
    - Learn about if, else, and elif statements.
    - Logical operators: and, or, not.
    Project:
    Build a simple age checker: Ask the user for their age and
    tell them if they are eligible for certain services
    (e.g., "You are eligible to vote" or "You are too young to vote").
"""

age = int(input('Please enter your age: '))
if (age < 18):
    print("You are not eligible to vote")

else:
    print("Registration Status: ")
    registration_status = int(input("Please enter 1 for Yes and 2 for No: "))

if (age >= 18) and (registration_status == 1):
    print("You are eligible to vote")
elif (age >= 18) and (registration_status==2):
    print("You are not eligible to vote")

