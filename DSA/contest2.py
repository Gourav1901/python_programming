t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    arr.sort()
    maxx = -1
    left = 0
    right = n - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum < k:
            maxx = max(maxx, current_sum)
            left += 1
        else:
            right -= 1
    if maxx == -1:
        print(-1)
    else:
        print(maxx)
    t -= 1