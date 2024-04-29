#Write a program to find the maximum and minimum value in an array of integers.

#   arr = [3,2,1,5,2]  = max = 5 , min =  1
#     max = arr[0]
#     min = arr[0]
#     3 > 3 = false = max = 3
#     3 < 3 = false = min = 3
#     2 > 3 = false = max = 3
#     2 < 3 = true = min = arr[i] = 2
#     1 > 3 = false = max = 3
#     1 < 2 = true  =  min = arr[i] = 1
#     5 > 3 = true = max = arr[i] = 5
#     5 < 1 = false  = min = 1
#     2 > 5 = false = max = 5
#     2 < 1 = false  = min  = 1

arr = [3,-2,-1,-5,2]
max = arr[0]
min = arr[0]
for i in arr:
  if max < i:
    max = i
  if min > i:
    min = i
print("max element:",max)
print("min element:",min)