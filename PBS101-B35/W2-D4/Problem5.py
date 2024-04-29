# promt the user to enter weight and height
weight = int(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Checking for invalid input
if weight <= 0 or height <= 0:
    print("Invalid input, weight and height must be positive numbers.")
elif height == 0:
    print("Invalid input, height cannot be zero.")
else:
    # Calculating BMI
    bmi = weight / (height * height)
    
    # Printing the result
    print("BMI:", round(bmi, 2))