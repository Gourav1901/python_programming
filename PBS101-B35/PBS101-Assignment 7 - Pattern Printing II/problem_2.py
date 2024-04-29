N = int(input())
c = (N*2) // 2
for i in range(N):
  print(" " * (N-i-1),end=" ")
  print("*" * (i + 1),end="")
  print("*" * i,end="")
  print()
print(" " * c + "|"  )