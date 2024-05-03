# Write a function named calculatePower that takes two integers, base, and exponent, as input and returns the result of raising the base to the exponent. Use this function to calculate the power of a given base and exponent.

# powerResult = calculatePower(2, 3);

# // Sample Output: powerResult = 8
def powerCalculation(base,exponent):
    powerResult = base ** exponent
    return powerResult

result = powerCalculation(2,3)
print(result)