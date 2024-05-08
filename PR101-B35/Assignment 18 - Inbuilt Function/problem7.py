# **Task:** Write a custom function that behaves similarly to Python's `str.count()` and `list.count()` methods. This function should count how many times a specific element appears in a string or a list.

# - **Sample Input (for list):** `[1, 2, 2, 3, 4, 2]`, `2`
# - **Sample Output:** `3`
# - **Sample Input (for string):** `'hello world'`, `'o'`
# - **Sample Output:** `2`
# - **Documentation:** [str.count()](https://docs.python.org/3/library/stdtypes.html#str.count) and [list.count()](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

def count(l1,K):
  count = 0
  for i in range(len(l1)):
    if l1[i] == K:
      count += 1
  return count
list1 = [1, 2, 2, 3, 4, 2]
value = 2
string = "Hello, World!"
ch = 'o'
print(count(list1,value))
print(count(string,ch))