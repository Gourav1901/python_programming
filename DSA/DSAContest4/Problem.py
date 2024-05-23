s = input()
m = {}

for i in s:
    if i in m:
        m[i] += 1
    else:
        m[i] = 1
    
for key,pair in sorted(m.items()):
    print(f"{key} {pair}")