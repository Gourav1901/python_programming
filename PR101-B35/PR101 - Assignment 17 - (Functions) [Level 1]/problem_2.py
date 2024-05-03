# Find Maximum
# Write a function named findMinMax that takes an array of numbers as input and returns maximum value." The values should be the maximum numbers in the input array, respectively.
# Sample Input: arr = [15, 2, 34, 8, 19]
# Sample Output: max = maximum(arr) ; // output: max = 34 ;
def maximum(arr):
    max1 = arr[0]
    for i in range(len(arr)):
        if max1 < arr[i]:
            max1 = arr[i]
    print(max1)

arr = [15,2,34,8,19]
maximum(arr)