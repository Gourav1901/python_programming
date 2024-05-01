# ### Problem 1: Set Union Without Duplicates
# **Description:** Write a Python program to perform the union of three sets without using the built-in union method. Ensure there are no duplicates in the final set.

set1 = {1,2,3}
set2 = {3,4,5}
set3 = {5,6,7}
ans = set1.union(set2).union(set3)
print(ans)
