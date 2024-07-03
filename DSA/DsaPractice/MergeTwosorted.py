def merge(n,arr,arr2):
    s = 0
    f = 0
    res = []
    while s < n and f < n:
        if arr[s] <= arr2[f]:
            res.append(arr[s])
            s +=1
        elif arr2[f] < arr[s]:
            res.append(arr2[f])
            f += 1
    while s < n:
        res.append(arr[s])
        s += 1
    while f < n:
        res.append(arr2[f])
        f += 1
    return res    
            

n = int(input())
arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

ans  = merge(n,arr,arr2)
print(*ans)