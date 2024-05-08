# def solve(N, K, s):
#     summ = 0
#     dict_T = {}
#     for i in range(0,26):
#         for j in range(i,26):
#             dict_T[chr(ord("a") + i)] = N + i
#     for i in s:
        
#         for key, value in dict_T.items():
#             if key == i:
                
#                 summ += value
#     print(summ)
# def solve(string):
    
#     max_len = 0
#     n = len(string)

#     for i in range(n):
#         for j in range(i+1,n+1):
#             sub = string[i:j]
#             check = sub[::-1]
#             if sub == check:
#                 if len(sub) > max_len:
#                    max_len = len(sub) 
#     print(max_len)

# def solve(N,A):
#     total_sum = sum(A)
#     min_index = -1
#     min_element = float('inf')
#     for i in range(N):
#         if (total_sum - A[i]) % 7 == 0 and A[i] < min_element:
#             min_element = A[i]
#             min_index = i
#     print(min_index)
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True



# def solve(N,arr):
#     total_sum = 0
#     for i in range(N):
#         for j in range(i+1,N):
#             if is_prime(j-i):
#                 total_sum += abs(arr[i] - arr[j])
#     print(total_sum)