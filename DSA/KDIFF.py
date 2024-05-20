t = int(input())
for _ in range(t):
    n,K = map(int, input().split())
    
    arr = list(map(int,input().split()))
    arr.sort()
    s = 0
    e = 1
    
    flag = False
    while s < n and e <n:
        if s != e and arr[e] - arr[s] == K:
            flag = True
            break
        elif arr[e] - arr[s] < K:
            e += 1
        else:
            s += 1
    if flag:
        print("Yes")
    else:
        print("No")
    