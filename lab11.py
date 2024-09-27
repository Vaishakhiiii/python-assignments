'''1. Print the first 10 natural numbers using a for loop:
python'''

# Print the first 10 natural numbers
for i in range(1, 11):
    print(i)

    
'''2. Python program to check if the given string is a palindrome:
python'''

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Convert the string to lowercase to ignore case sensitivity
    s = s.lower()
    # Compare the string with its reverse
    return s == s[::-1]

# Input from the user
string = input("Enter a string: ")

if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")

    
'''3. Python program to check if a given number is an Armstrong number:
python'''

# Function to check if a number is an Armstrong number
def is_armstrong(num):
    # Convert the number to a string to get the number of digits
    num_str = str(num)
    power = len(num_str)
    # Calculate the sum of digits raised to the power
    armstrong_sum = sum(int(digit) ** power for digit in num_str)
    return armstrong_sum == num

# Input from the user
number = int(input("Enter a number: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

    
'''4. Python program to get the Fibonacci series between 0 to 50:
python'''

# Function to generate the Fibonacci series up to 50
def fibonacci_series(limit=50):
    a, b = 0, 1
    while a <= limit:
        print(a, end=" ")
        a, b = b, a + b
    print()  # For new line after series ends

# Call the function
fibonacci_series()


'''5. Python program to check the validity of password input by users:
python'''

import re

# Function to check the validity of a password
def check_password_validity(password):
    # Checking the length of the password (6 to 12 characters)
    if len(password) < 6 or len(password) > 12:
        return "Invalid! Password length should be between 6 and 12 characters."

    # Checking for at least one uppercase letter, lowercase letter, digit, and special character
    if not re.search("[a-z]", password):
        return "Invalid! Password must contain at least one lowercase letter."
    if not re.search("[A-Z]", password):
        return "Invalid! Password must contain at least one uppercase letter."
    if not re.search("[0-9]", password):
        return "Invalid! Password must contain at least one digit."
    if not re.search("[@#$]", password):
        return "Invalid! Password must contain at least one special character (@, #, or $)."
    
    # If all conditions are met, the password is valid
    return "Password is valid."

# Input password from the user
user_password = input("Enter a password: ")

# Check the validity of the password
result = check_password_validity(user_password)
print(result)
