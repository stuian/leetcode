def canWinNim(n):
    """解法一，动态规划"""
    if n <= 3:
        return True
    dp = [False] * n
    dp[0], dp[1], dp[2] = True, True, True
    for i in range(3, n):
        if not dp[i - 1] or not dp[i - 2] or not dp[i - 3]:
            dp[i] = True
    return dp[-1]

if __name__ == '__main__':
    print(canWinNim(8))
