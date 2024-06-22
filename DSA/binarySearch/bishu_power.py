def bishu(soldiers, power, prefix):
  low = 0
  high = len(soldiers) -1
  while (low <= high):
    mid = (low + high)//2
    
    if soldiers[mid] <= power:
      res = mid
      low = mid + 1
    else:
      high = mid -1 

  return "{} {}".format(res + 1,prefix[res])




n = int(input())

soldiers = []

for i in range(n):
  soldiers.append(int(input()))

soldiers.sort()

ans = []

pref = []

s = 0
for i in soldiers:
  s =s +i
  pref.append(s)

for q in range(int(input())):
  power = int(input())

  ans.append(bishu(soldiers,power,pref))

for i in ans:
  print(i)
