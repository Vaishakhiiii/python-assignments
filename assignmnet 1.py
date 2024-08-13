#Assignment Questions:

#1. Calculate the multiplication and sum of two numbers
a =5
b = 2
sum = a+b
multiplication = a*b
print(sum)
print(multiplication)

#2. Declare two variables and print that which variable is largest using ternar operator
a = 13
b  = 28
a_largest = True if a>b else False
b_largest = True if b>a else False
print(a_largest)
print(b_largest)

#Python program to convert the temperature in degree centigrade to Fahrenheit
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input from the user
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Display the result
print(f"{celsius}°C is equal to {fahrenheit}°F")

#4. Python program to find the area of a triangle whose sides are given
def area_of_triangle(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

try:
    # Input the sides of the triangle
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    
    # Check if the input lengths form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate and print the area
        print(f"The area of the triangle is: {area_of_triangle(a, b, c)}")
    else:
        print("The lengths provided do not form a valid triangle.")
except ValueError:
    print("Please enter valid numeric values.")




