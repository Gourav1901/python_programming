# **Task:** Develop a custom function that reverses the order of items in a list or characters in a string, similar to Python's `reversed()` function or the `[::-1]` slice shortcut.

# - **Sample Input (for list):** `[1, 2, 3, 4, 5]`
# - **Sample Output:** `[5, 4, 3, 2, 1]`
# - **Sample Input (for string):** `'hello'`
# - **Sample Output:** `'olleh'`
# - **Documentation:** [reversed()](https://docs.python.org/3/library/functions.html#reversed)

def reverse(l1):

  l2 = []
  for i in range(len(l1)-1,-1,-1):
    l2.append(l1[i])
  return l2

def rev(l1):
  res = ""
  for i in range(len(l1)-1,-1,-1):
    res += l1[i]
  return res

list1 = [1,2,3,4,5]

string = "Hello"

print(reverse(list1))
print(rev(string))