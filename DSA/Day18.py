# Problem1
# def solve(S):
#     summ = 0
#     for char in S:
#         summ += ord(char) - ord('a') + 1
#     print(summ)

#problem2
# def solve(string):
#     s = ""
#     for i in range(len(string)):
#         if string[i] == "#" and i > 0:
#             s = s[:-1] 
#         elif string[i] != "#":
#             s += string[i]
#     print(s)

#problem3
# def solve(S,K):
#     en = ""
#     for char in S:
#         if char.isalpha():
#             sift = 97 if char.islower() else 65
#             en += chr((ord(char) - sift + K) % 26 + sift)
#         elif char.isdigit():
#             en += str((int(char) + K ) % 10)
#         else:
#             en += char
            
#     print(en,end="")

# def is_prime(l1):
#   if l1 > 1:
#     is_prime = True
#     for k in range(2,l1):
#       if l1 % k == 0:
#         is_prime = False
#         break
#     return is_prime
       
# string = "abc"
# n = len(string)

# for i in range(n):
#   for j in range(i+1,n+1):
#     l1 = len(string[i:j])
#     if is_prime(l1):
#       print(string[i:j])

# string = "100100000011"
# max = 0

# n = len(string)
# for i in range(n):
#   for j in range(i+1,n+1):
#     sub = string[i:j]
#     if "1" in sub:
#         continue
#     else:
#        if len(sub) > max :
#           max = len(sub)
# print(max)

# string = "abababababab"
# count = 0
# n= len(string)
# for i in range(n):
#   for j in range(i,n):
#     if string[i] == string[j]:
#       count += 1
# print(count)

      
# string = ""
# k = "a"
# count = 0
# n= len(string)
# for i in range(n):
#   for j in range(i+1,n+1):
#     sub = string[i:j]
#     if sub[0] == k:
#       count += 1
# print(count)


      
        
# string = "theracecarisgood"
# max_len = 0
# n = len(string)

# for i in range(n):
#   for j in range(i+1,n+1):
#     sub = string[i:j]
#     check = sub[::-1]
#     if sub == check:
#       if len(sub) > max_len:
#         max_len = len(sub) 
# print(max_len)

# arr = [1,2,1,3,4]
# n = len(arr)
# k = 3
# flag = False
# for i in range(n):
#   for j in range(i+1,n+1):
#     subarr = arr[i:j]
#     summ = sum(subarr)
#     if summ == k:
#       flag = True
# print(flag)
       
    
      
# def solve(N,K, arr):
#     sorted_arr = sorted(arr)
#     s = 0
#     end = N-1
#     count = 0
#     print(sorted_arr)
#     while s < end:
#         if sorted_arr[s] + sorted_arr[end] == K:
#             count += 1
#             s += 1
            
#         else:
#             end -= 1
       
#     print(count)
# arr = [3,0,6,2,7]
# N = 5
# K = 9
# solve(N,K,arr)
    


       
        
     
   




       
