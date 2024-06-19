arr = [3 , 5,6,-7,5]

k = 6

arr.sort()

s = 0
e = len(arr)-1

while(s<e):
  mid = s+ (e + s)/2

  if arr[mid] == k:
    print(mid)
    
  elif arr[mid] > k:
    s = mid + 1
  else:
    e = mid - 1
    