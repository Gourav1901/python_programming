def MaxMin(arr,n):
    for i in range(n) :
        isSwapped = 0
        for j in range(n-i-1):
            if arr[j] > arr[j+1] :
                arr[j],arr[j+1] = arr[j+1],arr[j]
                isSwapped = 1
        if isSwapped != 1 :
            break
    dictionary = {}
    for ele in arr :
        dictionary[ele] = ele
        
    change = list(dictionary)
    firstThree = change[:3]
    lastThree = change[-3:]
    
    if len(firstThree) < 3 :
        print("Not Possible")
    else :
        print(*firstThree)
    if len(lastThree) < 3 :
        print("Not Possible")
    else :
        print(*lastThree)





n = int(input())

arr = list(map(int,input().split()))

MaxMin(arr,n)





