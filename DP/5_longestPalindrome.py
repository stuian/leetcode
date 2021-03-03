class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_substr = ""
        dp = [[False] * n for _ in range(n)]
        for i in range(n): # 子串的长度 i+1
            for j in range(n):
                if j == i:
                    dp[i][j] = True
                if i-j+1 == 2 and s[i]==s[j]:
                    dp[i][j] = True
                if i-j+1 > 2:
                    if dp[i-1][j+1] and s[i]==s[j]:
                        dp[i][j] = True
                if dp[i][j] and ((i-j+1) > len(max_substr)):
                    max_substr = s[j:i+1]
        return max_substr

def main():
    test = Solution()
    result = test.longestPalindrome("cbbd")
    print(result)

if __name__ == '__main__':
    main()