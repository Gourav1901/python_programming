t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    m = int(input())
    arr1 = list(map(int,input().split()))
    r =[]
    s = 0
    e = 0
    
    while s < n and e < m:
        if arr[s] == arr1[e]:
            r.append(arr[s])
            s += 1
            e += 1
        elif arr[s] < arr1[e]:
                s += 1
                
        else:
            e += 1
    if len(r) == 0:
        r.append(-1)
    for i in range(len(r)):
        print(r[i],end=" ")
    print()