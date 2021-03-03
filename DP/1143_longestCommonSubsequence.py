import numpy as np

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1 = list(text1)
        t2 = list(text2)
        dp = np.zeros((len(t1),len(t2)),dtype=np.int)
        for j in range(len(t2)):
            if t2[j] == t1[0]:
                dp[0,j:] = 1
                break
        for i in range(len(t1)):
            if t1[i] == t2[0]:
                dp[i:,0] = 1
                break
        for i in range(1,len(t1)):
            for j in range(1,len(t2)):
                if t1[i]==t2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return int(dp[len(t1)-1,len(t2)-1])


def main():
    test = Solution()
    text1 = "abc"
    text2 = "def"
    result = test.longestCommonSubsequence(text1,text2)
    print(result)
    print(type(result))

if __name__ == '__main__':
    main()