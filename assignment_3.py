#1. Program to accept two numbers and calculate their squares:

Number1= int(input("Enter the number1: "))
Number2= int(input("Enter the number2: "))

square1 = Number1 ** 2
square2 = Number2 ** 2

print(f"square of {Number1} is {square1}")
print("square of ",Number2,"is",square2)

#2. Program to check if a number is even or odd using a ternary operator:

Number = int(input("Enter the number: "))

Result = "Even" if Number % 2 == 0 else "odd"
print(f"The Number {Number} is {Result}")
