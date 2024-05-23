t = int(input())


    
def is_prime(num):
    if num > 1:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
        return True 
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    maxx = 0
    for i in range(n):
        for j in range(i+1,n+2):
            sub = arr[i:j]
            summ = sum(sub)
            if summ > 1 and is_prime(summ):
                if len(sub) > maxx:
                    maxx = len(sub)
    print(maxx)
                