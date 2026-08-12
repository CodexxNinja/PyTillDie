#Checking Number is Positive, Negative or Zero

num = int(input("Enter a number: "))

if num < 0:
    print(f'{num} is a Negative Number.')
elif num > 0:
    print(f'{num} is a Positive Number.')
else:
    print(f'{num} is a Zero.')
