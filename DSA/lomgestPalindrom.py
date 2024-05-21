def longestPalindrome(self, s: str) -> str:
        max_len = 0
        n = len(s)
        ans = ""
        if n == 1:
            return s
        for i in range(n):
            for j in range(i+1,n+1):
                sub = s[i:j]
                check = sub[::-1]
                if sub == check:
                    if len(sub) > max_len:
                        max_len = len(sub)
                        ans = sub 
        return ans
