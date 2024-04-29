
# Prompting the user to input the base and height 
base, height = map(int, input("Enter the base and height: ").split())

# Checking if either the base or height is zero
if base == 0 or height == 0:
    # If either is zero, the area of the triangle is also zero
    print(0.0) 
# Checking if either the base or height is negative
elif base < 0 or height < 0:
    # If either is negative, it's an invalid input 
    print("Invalid input, base and height must be positive numbers.")
else:
    # If both base and height are positive, calculating the area of the triangle
    Area = (base * height) / 2
    # Printing the calculated area
    print(Area)
