t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    
    dict_T = {}
    flag = "NO"
    for i in arr:
        if i in dict_T:
            dict_T[i] += 1
        else:
            dict_T[i] = 1
    for value in dict_T.values():
        if value > 1:
            flag = "YES"
            break
    print(flag)