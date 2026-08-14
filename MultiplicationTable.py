# Printing multiplication table of a number
n = int(input("Enter a number: "))

print("Multiplication table of",n,"is:")
for i in range(1,11):
    print(f'{n}X{i}:{n*i}')
