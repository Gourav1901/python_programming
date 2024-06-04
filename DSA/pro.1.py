n = int(input())
s = input()
c = 0
v = "aeiou"
for i in s:
    if i in v:
       c += 1
if c >= n//2:
    print("Feel good!")
else:
    print("Feel bad!")