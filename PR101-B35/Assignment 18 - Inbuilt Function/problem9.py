# **Task:** Write a custom function that replicates the behavior of the `str.find()` method. This function should search for a substring within a string and return the index of the first occurrence. If the substring is not found, it should return `-1`.

# - **Sample Input:** `'Look for the substring in this string.'`, `'substring'`
# - **Sample Output:** `12`
# - **Documentation:** [str.find()](https://docs.python.org/3/library/stdtypes.html#str.find)
def custom_find(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            return i-1
    return -1


string = 'Look for the substring in this string.'
substring = 'substring'
print(custom_find(string, substring)) 