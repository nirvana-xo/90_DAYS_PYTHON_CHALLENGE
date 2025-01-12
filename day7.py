"""
Day 7: Dictionaries and Sets
Topics:
 - Learn about dictionaries (key-value pairs) and sets (unordered collections).
 - Dictionary methods: get(), keys(), values().
Project:
 - Create a program that stores user information (name, age) in a dictionary and allows the user to 
retrieve it by providing the name
"""
name = input("Please enter you name: ")
age = int(input("PLease enter your age: "))

person_dict = {
    'name' : name,
    'age': age
}


print(f"Your name is {person_dict['name']} and you are {person_dict['age']} years old.")
