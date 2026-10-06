# Swap two variables using a third variable

a = 10
b = 20

temp = a
a = b
b = temp

print("a =", a)
print("b =", b)


#Swap two variables without a third variable

a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)