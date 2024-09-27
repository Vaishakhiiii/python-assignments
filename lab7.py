#1 Check if a number is even or odd using a ternary operator:
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number is {result}.")

#2 Swap two numbers:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print(f"After swapping, first number: {a}, second number: {b}")

#3 Convert kilometers to miles:
km = float(input("Enter distance in kilometers: "))
conversion_factor = 0.621371
miles = km * conversion_factor

print(f"{km} kilometers is equal to {miles} miles.")

#4 Calculate Simple Interest:
principal = 200  # Rs. 200
rate = 5         # 5% per year
time = 5         # 5 years

simple_interest = (principal * rate * time) / 100
print(f"The Simple Interest is Rs. {simple_interest}.")
