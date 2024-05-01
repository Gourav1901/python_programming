# ### Problem 5: Maximum and Minimum in a Tuple
# **Description:** Write a Python program to find the maximum and minimum numbers in a tuple of integers without using the built-in `max()` and `min()` functions.
# **Sample Input:** `(5, 10, 3, 15, 2, 20)`

tp = (5,10,3,15,2,20)
max = tp[0]
min = tp[0]
for i in tp:
  if i > max:
    max = i
  if i < min:
    min = i
print("max:",max)
print("min:",min)
