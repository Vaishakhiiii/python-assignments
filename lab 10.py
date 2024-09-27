'''1. Print the reverse order series  using a while loop'''

num = 10
while num > 0:
    print(num)
    num -= 1

'''2.Create a code that describe the use of break statement in while loop'''
counter = 0
while True:
    counter += 1
    if counter == 5:
        print("Breaking the loop")
        break  
    print(counter)
    
'''3. Iterate through each character of the string "Python" and print each
character on a new line. Additionally, calculate and print the length of the string.'''

s = "Python"
index = 0
while index < len(s):
    print(s[index])
    index += 1
print("Length of the string:", len(s))


'''4. Write a Python program that takes an integer input from the user and calculates
its factorial using a while loop. Display the result as the factorial of the entered
number.'''

num = int(input("Enter an integer: "))
factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print("Factorial is:", factorial)

'''Assignment'''

'''1. Write a python program to reverse a number using a while loop.'''
num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed number is:", reversed_num)


'''2. Write a python program to check whether a number is palindrome or not?'''
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if original_num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

'''3. Write a python program finding the factorial of a given number using a while loop.'''
num = int(input("Enter a number: "))
factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print("Factorial is:", factorial)


'''4.Accept numbers using input() function until the user enters 0.
Then break the loop and display the sum of all the numbers.'''
total_sum = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total_sum += num

print("Sum of all numbers:", total_sum)


'''5.Check whether the given number is an Armstrong number or not.'''
num = int(input("Enter a number: "))
temp = num
sum_of_powers = 0
num_of_digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_of_digits
    temp //= 10

if num == sum_of_powers:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")







