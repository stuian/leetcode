import numpy as np
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s = list(s)
        n = len(s)
        if n <= 1:
            return n
        dp = np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i,j] = 1
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[i,j] = dp[i+1,j-1] + 2
                else:
                    dp[i,j] = max(dp[i+1,j],dp[i,j-1])
        return int(dp[0,n-1])