"""
Topics:
- Learn how to read and write files in Python using open(), read(), write().
 - Working with text and CSV files.
Project:
 - Write a script that reads a text file and counts how many lines and words are in the file.
"""


with open('ass.txt', "r") as file:
    lines = file.readlines()  # Read all lines
        
        # Count the number of lines
    line_count = len(lines)
        
        # Count the number of words
    word_count = sum(len(line.split()) for line in lines)
        
        # Print the results
    print(f"Total Lines: {line_count}")
    print(f"Total Words: {word_count}")

