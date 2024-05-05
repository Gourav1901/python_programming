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





       
