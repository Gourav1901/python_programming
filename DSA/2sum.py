t = int(input())
while t > 0:
    n,k = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    s = 0
    e = n-1
    arr.sort()
    found = False
    while s < e:
        if arr[s] + arr[e] == k:
            
            found = True
            break
        elif arr[s] + arr[e] > k:
            e -= 1
        else:
            s += 1
    if not found:
        print(-1)
    else:
        print(1)
    
    t -= 1
            