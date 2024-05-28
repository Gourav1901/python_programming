arr = [12,18,17,65,46]
k = 6 
l = []
for i in range(len(arr)):
     l.append(arr[i] % k)

for i in range(len(l)-2):
     for j in range(len(l)-1):
          if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
                

for i in l:
     print(i,end=" ")