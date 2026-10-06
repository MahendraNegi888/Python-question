#Count Vowels in a String

text = input("Enter a string: ")

count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        count += 1

print("Number of vowels =", count)

#count charcters in a string

text = input("Enter a string: ")

print("Number of characters =", len(text))

#uppercase to lowercase

text = input("Enter a string: ")

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())