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