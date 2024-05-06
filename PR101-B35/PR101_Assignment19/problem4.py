# List Multiples of a Number
# Write a function named listMultiples that takes two numbers n and limit. The function should print the first n multiples of limit.
# E.g., listMultiples(3, 5) should print 3, 6, 9, 12, 15

def listMultiples(n, limit):
    for i in range(1, n + 1):
        print(i * limit, end=" ")


listMultiples(5, 3)