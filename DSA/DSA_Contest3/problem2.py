n = int(input())
arr1 = list(map(int, input().split()))

q = int(input())
arr2 = list(map(int,input().split()))
flag = False
# for i in range(q):
#     for j in range(n):
#         if arr2[i] == arr1[j]:
#             flag = True
#             break
#     if flag == True:
#         print("YES")
#     else:
#         print("NO"
m = {num:True for num in arr1}
for i in arr2:
    if i in m:
        print("YES")
    else:
        print("NO")