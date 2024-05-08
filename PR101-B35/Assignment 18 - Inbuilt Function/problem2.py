# **Task:** Create a custom function that behaves like Python's built-in method for finding the last index of an item in a list. If the item is not found, your function should return `-1`.
# **Sample Input:** `[1, 2, 3, 2, 4]`, `2`
# **Sample Output:** `3`
# **Documentation:** There's no direct equivalent in the list methods, but you can refer to [list methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) for inspiration.

def reindex(l1,T):
  for i in range(len(l1)-1,-1,-1):
    if T == l1[i]:
      return(i)
    
  else:
      return(-1)
  
l1 = [1, 2, 3, 2, 2]
Target = 2
print(reindex(l1,Target))