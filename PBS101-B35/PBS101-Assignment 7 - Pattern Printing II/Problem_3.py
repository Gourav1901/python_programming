H = int(input())
W = int(input())

for i in range(H):
  for j in range(2*W):
    if i % 2 == 0:
      if j % 2 == 0:
        print("[]",end="")
      else:
        print(" ",end=" ")
    else:

      if j % 2 != 0:
        print("[]",end="")
      else:
        print(" ",end=" ")
  print()
    