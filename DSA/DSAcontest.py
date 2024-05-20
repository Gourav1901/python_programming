t = int(input())
for _ in range(t):
    N = int(input())
    water_volume = list(map(int,input().split()))
    capacities = list(map(int,input().split()))
    
    total_water = sum(water_volume)
    if N ==2 :
        max1, max2 = capacities[0],capacities[1]
    else:
        max1, max2 = 0, 0
        for capacity in capacities:
            if capacity > max1:
                max2 =max1
                max1 = capacity
            elif capacity > max2:
                max2 = capacity
    if max1 + max2 >= total_water:
        print("YES")
    else:
        print("NO")