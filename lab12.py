# Accept the number of rows from the user
rows = int(input("Enter the number of rows: "))

# Pattern 1: Increasing star pattern
print("\nPattern 1:")
for i in range(1, rows + 1):
    print('*' * i)

# Pattern 2: Decreasing star pattern
print("\nPattern 2:")
for i in range(rows, 0, -1):
    print('*' * i)

# Pattern 3: Right-aligned increasing star pattern
print("\nPattern 3:")
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * i)

# Pattern 4: Right-aligned decreasing star pattern
print("\nPattern 4:")
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * i)

# Pattern 5: Binary pattern
print("\nPattern 5:")
for i in range(rows):
    start = 1 if i % 2 == 0 else 0
    for j in range(rows - i):
        print(start, end="")
        start = 1 - start
    print(' ' * i)

# Pattern 6: Diamond-inverted pyramid star pattern
print("\nPattern 6:")
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
