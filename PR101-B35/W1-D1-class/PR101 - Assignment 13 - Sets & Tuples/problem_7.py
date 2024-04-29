# Given a list of numbers, write a Python program to remove all duplicates and return a tuple with the remaining elements sorted in ascending order.
# **Sample Input:** `[1, 2, 3, 4, 3, 2, 1]`
# **Sample Output:** `(1, 2, 3, 4)`
li = [1, 2, 3, 4, 3, 2, 1]

# Remove duplicates
uni = []
for num in li:
    if num in uni:
        continue
    uni.append(num)
uni.sort()
sorted_tuple = tuple(uni)
print(sorted_tuple)