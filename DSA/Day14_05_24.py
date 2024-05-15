# N, M = map(int, input().split())

# arr = []
# for i in range(N):
#     arr1 = []
#     arr.append(input())
#     for j in range(M):
#         arr1.append(input())
#     arr.append(arr1)
# print(arr)
# n = int(input())
# arr =[]
# for i in range(n):
#   arr.append(input())
# for i in arr:
#   print(i,end=" ")

# n,m = map(int,input().split())
# arr =[]
# for i in range(n):
#     arr.append(list(map(int,input().split())))
# print(arr)

#solve some qus 
# N, M = map(int, input().split())

# arr = []
# for i in range(N):
#     arr.append(list(map(int,input().split())))
# for i in range(M):
#     pro = 1
#     for j in range(N):
        
#         pro *=(arr[j][i])
#     print(pro)   


#qus to find out occrence of a no maxi time in an array
n = int(input())
arr = list(map(int,input().split()))

dict_T = {}
for i in range(n):
    if arr[i] not in dict_T:
        dict_T[arr[i]] = 1
    else:
        dict_T[arr[i]] += 1
    
    maxx = 0
    occ = 0
    for key, value in dict_T.items():
        if value > maxx :
            maxx = value
            occ = key
print(occ)


