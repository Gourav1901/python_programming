n = int(input())

if n > 1:
  flag  = True

for i in range(2,n):
  if n % i == 0:
    flag = False
    break
print(flag)