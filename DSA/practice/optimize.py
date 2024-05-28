arr = [12,18,17,65,46]
k = 6 


for i in range(len(arr)-2):
     for j in range(len(arr)-1):
          if arr[j]%k>arr[j+1]%k:
            arr[j],arr[j+1] = arr[j+1],arr[j]
                

for i in arr:
     print(i,end=" ")