# **Description:** Given two sets, write a Python program to perform the following operations:
# - Print their union.
# - Print their intersection.
# **Sample Input:**
# - Set 1: `{1, 2, 3, 4, 5}`
# - Set 2: `{4, 5, 6, 7, 8}`
# **Sample Output:**
# - Union: `{1, 2, 3, 4, 5, 6, 7, 8}`
# - Intersection: `{4, 5}`

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
uni = set1.union(set2)
inter = set1.intersection(set2)
print("Union:", uni)
print("Intersection:", inter)