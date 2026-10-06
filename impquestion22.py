#largest element in a list

numbers = [10, 25, 5, 40, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest =", largest)


#smallest element in a list

numbers = [10, 25, 5, 40, 15]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest =", smallest)