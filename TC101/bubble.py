arr = [2,6,3,5,9,5,4]

for i in range(len(arr)-1):
  for j in range(i+1,len(arr)-1):
    if arr[j] > arr[j+1]:
      arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)


 