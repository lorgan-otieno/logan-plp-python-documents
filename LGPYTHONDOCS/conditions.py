# Function to validate if the input consists only of alphabetic characters
def is_valid_name(name):
    return name.isalpha()

# Prompt the user to enter their name
while True:
    name = input("Enter your name: ")
    if is_valid_name(name):
        break  # Exit the loop if the input is valid
    else:
        print("Invalid input. Please enter a valid name consisting only of alphabetic characters.")

# Continue with the rest of the program
# Prompt the user to enter their age
age = int(input("Enter your age: "))

# Check if the age is greater than or equal to 18
if age >= 18:
    print(f"hello {name}, You are eligible to vote.")
else:
    print(f"hello {name}, You are not eligible to vote.")
