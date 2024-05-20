t = int(input())
for _ in range(t):
     
    n = int(input())
    arr = list(map(int,input().split()))
     
    output = [1] * n
     
    s = 1
    e = 1
     
    for i in range(n):
        output[i] *= s
        s *= arr[i]
         
        output[n-1-i] *= e
        e *= arr[n-1-i]
    for i in output:
        print(i,end =" ")
    print()