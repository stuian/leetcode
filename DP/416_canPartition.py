class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0 or len(nums) <= 1:
            return False
        s = s // 2
        dp = [[False]*(s+1) for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = True
        for i in range(1,len(nums)+1):
            for j in range(1,s+1):
                if j-nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[len(nums)][s]