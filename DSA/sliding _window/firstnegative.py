def printFirstNegativeInteger( A, N, K):
    
    i = 0
    j = 0
    l = []
    res = []
    
    while j < N:
        if A[j] < 0:
            l.append(A[j])
        
        if (j - i + 1) != K:
            j += 1
        elif (j - i + 1) == K:
            if not l:
                res.append(0)
            else:
                res.append(l[0])
                if A[i] < 0:
                    l.pop(0)
            i += 1
            j += 1
    
    return res