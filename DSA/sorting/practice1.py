def custom_sort(arr,n,k):
    new_arr = sorted(arr,key = lambda ele : ele % k)
    return new_arr
    
n,k = map(int,input().split())
arr = list(map(int,input().split()))

ans = custom_sort(arr,n,k)
print(*ans)