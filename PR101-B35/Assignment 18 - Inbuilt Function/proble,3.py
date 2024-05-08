# **Task:** Write a custom function that simulates the behavior of slicing a list in Python. The function should take three parameters: the list to be sliced, the start index, and the end index, and return a new list.

# - **Sample Input:** `[1, 2, 3, 4, 5]`, `1`, `4`
# - **Sample Output:** `[2, 3, 4]`
#  **Documentation:** [Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)

def slic(li,start,end):
  result = []
  for i in range(start,end):
    result.append(li[i])
  return result

list_1 = [1, 2, 3, 4, 5] 
start = 1
end = 4
print(slic(list_1,start,end))