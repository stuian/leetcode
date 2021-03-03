class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]表示以nums[i]结尾的最长递增子序列
        if len(nums) == 0:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
        return max(dp)