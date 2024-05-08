def z_trv(mat):
  n = len(mat)

  for i in range(n):
    print(mat[0][i],end = " ")
  
  for j in range(1,n-1):
    print(mat[j][n-j-1],end = " ")

  for k in range(n):
    print(mat[n-1][k],end =" ")
  print()

def n_trv(mat):
  n = len(mat)
  for j in range(n-1,-1,-1):
    print(mat[j][0],end=" ")
  for i in range(1,n-1):
    print(mat[i][n-i-1],end=" ")
  for k in range(n-1,-1,-1):
    print(mat[k][n-1],end =" ")

def sk_trv(mat):
  n = len(mat)
  
mat = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]

z_trv(mat)
n_trv(mat)
sk_trv(mat)