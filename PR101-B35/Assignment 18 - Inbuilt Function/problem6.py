# **Task:** Create a custom function that mimics the behavior of the `list.index()` method in Python. This function should search a list for a specified value and return the index of the first occurrence. If the value is not found, your function should raise a ValueError.
# - **Sample Input:** `[1, 2, 3, 4, 5]`, `3`
# - **Sample Output:** `2`
# - **Documentation:** [list.index()](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

def index(li,k):
  for i in range(len(li)):
    if li[i] == k:
      return i
  else:
    return "valueError"

list1 = [1,2,3,4,5]
value = 3
print(index(list1,value))