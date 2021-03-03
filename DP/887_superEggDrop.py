class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # 现在面前有k个鸡蛋，允许测试m次，则最坏情况下可以测试一栋N层的楼
        # dp[k][m] = dp[k-1][m-1] + dp[k][m-1] + 1
        dp = [[0] for _ in range(K+1)] # (K+1)行一列
        m = 0
        while dp[K][m] < N:
            m += 1
            for k in range(K+1):
                dp[k].append(0)
                if k > 0:
                    dp[k][m] = dp[k-1][m-1]+dp[k][m-1] + 1
        return m