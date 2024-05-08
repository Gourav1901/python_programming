# **Task:** Write a custom function that replicates the behavior of the `in` operator for lists, determining whether a list contains a certain element.
# - **Sample Input:** `[1, 2, 3, 4, 5]`, `3`
# - **Sample Output:** `True`
# - **Documentation:** [Expressions](https://docs.python.org/3/reference/expressions.html#membership-test-operations)

def contain(l1,k):
  for i in range(len(l1)):
    if l1[i] == k:
      return True
  else:
    return False

list1 = [1,2,3,4,5]
given  = 3
print(contain(list1,given))