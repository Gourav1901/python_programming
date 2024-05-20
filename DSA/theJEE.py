P1, C1, M1 = map(int,input().split())
P2, C2, M2 = map(int,input().split())

sum1 = P1 + C1 + M1
sum2 = P2 + C2 + M2

if sum1 > sum2:
    print("First")
elif sum1 == sum2:
    if M1 > M2:
        print("First")
    elif M1 == M2:
        if P1 > P2:
            print("First")
        else:
            print("Second")

    else:
        print("Second")
else:
    print("Second")