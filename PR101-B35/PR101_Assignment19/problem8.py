# Write a function named findGCD that takes two integers as input and returns their greatest common divisor (GCD). Use this function to find the GCD of two given numbers.
# gcdResult = findGCD(36, 48);
# // Sample Output: gcdResult = 12

def findGCD(a, b):
    while b:
        a, b = b, a % b
    return a

# Test the function
gcdResult = findGCD(36, 48)
print("GCD:", gcdResult)