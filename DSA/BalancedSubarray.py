t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    dict_T = {}
    dict_T[0] = -1
    c1,c2 = 0,0
    ans = 0
    
    for i in range(n):
        if(arr[i] == 0):
            c1 += 1
        else:
            c2 += 1
        if(dict_T.get(c1 - c2) == None):
            dict_T[c1 - c2] = i
        else:
            ans = max(ans, i - dict_T[c1 - c2])
    print(ans)