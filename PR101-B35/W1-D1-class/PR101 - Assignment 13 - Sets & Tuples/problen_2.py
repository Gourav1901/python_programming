# **Description:** Write a Python program to calculate the sum of all numbers in a given tuple.
# **Sample Input:** `(8, 2, 3, 0, 7)`
# **Sample Output:** `20`
# Sample input
tp = (8, 2, 3, 0, 7)
sum = 0
for number in tp:
  sum += number
print(sum)