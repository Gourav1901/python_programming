def merge(n,arr,arr1):
    l = []
    
    s = 0
    e = 0
    while(s < n and e < n):
        if(arr[s]<arr1[e]):
            l.append(arr[s])
            s += 1
        else:
            l.append(arr1[e])
            e += 1
    while s < n :
        l.append(arr[s])
        s += 1
            
    while e < n :
        l.append(arr1[e])
        e += 1        
    return l            




n = int(input())
 
arr = list(map(int,input().split()))
arr1 = list(map(int,input().split()))

ans = merge(n,arr,arr1)
print(*ans)
