# class Solution:

# 	def rowWithMax1s(self,arr, n, m):
	    
# 	    i = 0
# 	    j = m-1
# 	    res = -1
	    
# 	    while i < n and j >= 0:
# 	        if arr[i][j] == 1:
# 	            j -=1
# 	            res = i
# 	        else:
# 	            i += 1
# 	    return res

# class Solution:
#     def sortedMatrix(self,N,Mat):
#         l = []
#         for row in Mat:
#             for ele in row:
#                 l.append(ele)
#         l.sort()
        
#         ans = []
        
#         for i in range(N):
#             Row = []
#             for j in range(N):
#                 Row.append(l[i * N + j]) 
#             ans.append(Row)
#         return ans
#         #code here