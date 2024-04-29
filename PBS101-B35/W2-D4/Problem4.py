# promt the user to input principal, rate, and time
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the rate of interest per year: "))
time = int(input("Enter the time in years: "))

# Checking if any input value is negativ
if principal < 0 or rate < 0 or time < 0:
    print("Invalid input, all values must be non-negative.")
else:
    # Calculating simple interest
    simple_interest = (principal * rate * time) / 100
    
    #result
    print("The simple interest is:", simple_interest)