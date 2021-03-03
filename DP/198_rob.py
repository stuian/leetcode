class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        dp = nums.copy()
        if len(nums) <= 2:
            return max(nums)
        for i in range(2,len(nums)):
            dp[i] += max(dp[:i-1])
        return max(dp)