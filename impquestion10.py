#Reverse a String

text = input("Enter a string: ")

print("Reverse =", text[::-1])

#check palindrome

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")