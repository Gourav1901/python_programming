def maximumSumSubarray (self,K,arr,N):
        # code here 
        sum = 0
        maxi = 0
        i = 0
        j = 0
        while(j < N):
            sum += arr[j]
            if j-i+1 < K:
               
                j += 1
            elif j-i+1 == K:
                maxi = max(maxi,sum)
                sum = sum - arr[i]
                i += 1
                j += 1
        return maxi