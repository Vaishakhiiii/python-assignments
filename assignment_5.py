''''1. Declare a div() function with two parameters. Then call the function and pass
two numbers and display their division.'''

#declaring function
def div(a,b):
    return a/b

#call dev function and passing two values
result = div(100,2)
print(f"result of divison is: {result}")

'''Declare a square() function with one parameter.Then call the function and pass one
number and display the square of that number .'''

#declaring function
def square(a):
    return a**2

#calling square function and passing values
result = square(7)
print(f"The square of 7 is {result}")

'''3. Using max() and min() functions display the maximum and minimum of 5 random
numbers.'''

def find_max_min(num1, num2, num3, num4, num5):
    numbers = [num1, num2, num3, num4, num5]
    return max(numbers), min(numbers)

# Example numbers
max_num, min_num = find_max_min(23, 45, 12, 78, 34)
print("Maximum number:", max_num)
print("Minimum number:", min_num)

'''4. Accept a name from the user and display that in lower case using lower() function'''
# Accept a name from the user
name = input("Enter your name: ")

# Display the name in lower case
print(f"name in lowercase {name.lower()}")

'''5. Create a program which accept a choice from the user and accordingly do teh operation
Show the menu card of hotel like Starters main course deserts and than accept the choice and
accept the choice till user want to accept and at the end display the bill YOu can create your
own menu items and then display the price as wellat the end you need to display the order
item with price and total bill amount'''
# Function to display menu and get user choice
def display_menu():
    print("\n___Hotel Menu___")
    print("1. Starters")
    print("2. Main Course")
    print("3. Desserts")
    print("4. Exit and display bill")

# menus for each category
def display_starters():
    print("\n_Starters Menu_")
    print("1. Soup - Rs120")
    print("2. Spring Rolls - Rs150")
    print("3. Masala papad - Rs100")

def display_main_course():
    print("\n_Main Course Menu_")
    print("1. Garlic Noodles - Rs250")
    print("2. Pasta - Rs150")
    print("3. Pizza - Rs200")

def display_desserts():
    print("\n_Desserts Menu_")
    print("1. Ice Cream - Rs70")
    print("2. Brownie - Rs140")
    print("3. Cheesecake - Rs200")

# Function to get user's choice of items
def get_item_choice(menu):
    choice = int(input("Enter the item number: "))
    if menu == "starters":
        if choice == 1:
            return ("Soup", 120)
        elif choice == 2:
            return ("Spring Rolls", 150)
        elif choice == 3:
            return ("Masala Papad", 100)
    elif menu == "main_course":
        if choice == 1:
            return ("Garlic Noodles", 250)
        elif choice == 2:
            return ("Pasta", 150)
        elif choice == 3:
            return ("Pizza", 200)
    elif menu == "desserts":
        if choice == 1:
            return ("Ice Cream", 70)
        elif choice == 2:
            return ("Brownie", 140)
        elif choice == 3:
            return ("Cheesecake", 200)
    return None

# Function to display final bill
def display_bill(order_list, total):
    print("\n_Your Final Bill")
    for item, price in order_list:
        print(f"{item}: Rs{price}")  # Shows the item name and its price
    print(f"\nTotal Amount to Pay: Rs{total}")  # Shows the total cost

# Main program logic
def main():
    order_list = []
    total_amount = 0

    while True:
        display_menu()
        choice = int(input("\nEnter your choice (1-4): "))

        if choice == 1:
            display_starters()
            item, price = get_item_choice("starters")
            order_list.append((item, price))
            total_amount += price

        elif choice == 2:
            display_main_course()
            item, price = get_item_choice("main_course")
            order_list.append((item, price))
            total_amount += price

        elif choice == 3:
            display_desserts()
            item, price = get_item_choice("desserts")
            order_list.append((item, price))
            total_amount += price

        elif choice == 4:
            display_bill(order_list, total_amount)
            break
        
        else:
            print("Invalid choice! Please enter number between 1-4.")

if __name__ == "__main__":
    main()

        




