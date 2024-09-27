#1. Program to Accept a Password and Check if it's Correct
correct_password = "password1305"
password = input("Enter the password: ")

if password == correct_password:
    print("Password is correct!")
else:
    print("Incorrect password.")


#2.Write a program to accept a no from the user and check it is even or odd if
    #the no is even then check it is divisble by5 or not. and if no is odd then
    #check it is positive or negative (Nested)

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
    if number % 5 == 0:
        print(f"{number} is divisible by 5.")
    else:
        print(f"{number} is not divisible by 5.")
else:
    print(f"{number} is odd.")
    if number > 0:
        print(f"{number} is positive.")
    else:
        print(f"{number} is negative.")

#3. Accept marks of 5 subject and calculate the grade  (else if)


marks = float(input("Enter your marks (out of 100): "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"


print(f"Your grade is: {grade}")


#1. Python program to check leap year

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
#2. Python Program to Find the Largest Among Three Numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is: {num2}")
else:
    print(f"The largest number is: {num3}")

#3. Python Program to Check if a Number is Positive, Negative or 0

number = int(input("Enter the number: "))

if number > 0:
    print(f"The number {number} is positive.")
elif number == 0:
    print(f"The number {number} is zero.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print("Please enter a valid value.")

'''
#4 A toy vendor supplies three types of toys: Battery Based Toys, Key-based
Toys, and Electrical Charging Based Toys. The vendor gives a discount of
10% on orders for battery-based toys if the order is for more than Rs. 1000.
On orders of more than Rs. 100 for key-based toys, a discount of 5% is
given, and a discount of 10% is given on orders for electrical charging based
toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3
are used for battery based toys, key-based toys, and electrical charging based
toys respectively. Write a program that reads the product code and the order
amount and prints out the net amount that the customer is required to pay
after the discount.
'''
product_code = int(input("Enter product code (1 for Battery, 2 for Key, 3 for Electrical): "))
order_amount = float(input("Enter order amount: "))

if product_code == 1 and order_amount > 1000:
    discount = 0.10
elif product_code == 2 and order_amount > 100:
    discount = 0.05
elif product_code == 3 and order_amount > 500:
    discount = 0.10
else:
    discount = 0.00

net_amount = order_amount - (order_amount * discount)
print(f"Net amount after discount: {net_amount:.2f}")


'''
#5. A transport company charges the fare according to following table:
Distance Charges
1-50 8 Rs./Km
51-100 10 Rs./Km
> 100 12 Rs/Km
'''
def calculate_fare(distance):
  """
  Calculates the fare based on the distance traveled.

  Args:
    distance: The distance traveled in kilometers.

  Returns:
    The fare in rupees.
  """

  if distance <= 50:
    return distance * 8
  elif distance <= 100:
    return distance * 10
  else:
    return distance * 12

# Example usage
distance = float(input("Enter distance traveled in kilometers "))
fare = calculate_fare(distance)
print(f"The fare for {distance} km is {fare} rupees.")

































