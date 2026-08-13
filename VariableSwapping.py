# Program for swapping 2 variables.

a = 5
b = 2
temp = 0
print("Before Swapping, Values of a & b are: ")
print("a =",a,"b =",b)

print("")

# Swap using temp variable.
print("...Swapping using Temp Variable...")
temp = a
a = b
b = temp

print("After Swapping, Values of a & b are: ")
print("a =",a,"b =",b)

print("")

# Swap without using temp variable.
print("...Swapping without using Temp Variable...")
a = a + b
b = a - b
a = a - b

print("After Swapping, Values of a & b are: ")
print("a =", a, "b =", b)
