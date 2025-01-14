def get_user_input():
    try:
        # Prompt user for input
        user_input = input("Please enter a number: ")
        
        # Attempt to convert the input to an integer
        number = int(user_input)
        print(f"You entered the number: {number}")
    
    except ValueError:
        # Handle case where input is not an integer
        print("Oops! That was not a valid number. Please enter an integer.")
    
    except Exception as e:
        # Catch any other exception
        print(f"An unexpected error occurred: {e}")
    
    finally:
        # This block will always execute
        print("Thank you for using the program!")

# Call the function to test
get_user_input()
