import numpy as np
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not len(word1):
            return len(word2)
        if not len(word2):
            return len(word1)
        def dp(i,j,word1,word2):
            if i == -1:
                return j+1
            if j == -1:
                return i+1
            if word1[i] == word2[j]:
                return dp(i-1,j-1,word1,word2)
            else:
                return min(dp(i-1,j,word1,word2),dp(i,j-1,word1,word2),dp(i-1,j-1,word1,word2))+1
        return dp(len(word1)-1,len(word2)-1,word1,word2)