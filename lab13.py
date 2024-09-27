'''1. Write a Python program to count the occurrences of each word in a

given sentence

string = “To change the overall look of your document. To change the look

available in the gallery"'''

string = "To change the overall look of your document. To change the look available in the gallery"


words = string.lower().split()
word_count = {}


for word in words:
    word = word.strip(".,") 
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")


'''2. Write a Python program to remove a newline in Python

String = "\nBest \nDeeptech \nPython \nTraining\n"'''

string = "\nBest \nDeeptech \nPython \nTraining\n"

string_without_newlines = string.replace("\n", " ")

print("String after removing newlines:")
print(string_without_newlines)


'''3. Write a Python program to reverse words in a string

String = “Deeptech Python Training”'''

string = "Deeptech Python Training"
reversed_string = ' '.join(string.split()[::-1])

print("Reversed string:")
print(reversed_string)


'''4. Write a Python program to count and display the vowels of a given text

String=”Welcome to python Training”'''

string = "Welcome to python Training"
vowels = "aeiouAEIOU"
vowel_count = 0


found_vowels = []
for char in string:
    if char in vowels:
        found_vowels.append(char)
        vowel_count += 1


print(f"Number of vowels: {vowel_count}")
print("Vowels found:", ', '.join(found_vowels))




