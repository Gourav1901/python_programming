# Write a function named reverseString that takes a string as input and returns the reverse of the string. Use this function to reverse a given string.

# reversedString = reverseString("hello");

# // Sample Output: reversedString = "olleh"
def reverseString(string):
    rev = ''
    for i in range(len(string)-1,-1,-1):
        rev = rev + string[i]
    return rev

reversedString = "hello"
ans = reverseString(reversedString)
print(ans)