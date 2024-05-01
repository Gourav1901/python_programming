### Problem 4: Subset Verification
# **Description:** Write a Python program to check if a set is a subset of another set. Do not use the built-in method for subset verification.
# **Sample Input:**
# - Set 1 (potential subset): `{1, 2, 3}`
# - Set 2: `{1, 2, 3, 4, 5, 6}`
# **Sample Output:** `True`

set1 = {1,2,3,9}
set2 = {1,2,3,4,5,6}
flag =True
for i in set1:
  if i not in set2:
    flag = False
    break
print(flag)