# Prompting the user to input two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Comparing the numbers
if number1 > number2:
    print(number1, "is larger than", number2)
elif number2 > number1:
    print(number2, "is larger than", number1)
else:
    print("Both numbers are equal")