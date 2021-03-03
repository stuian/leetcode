class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 二维的最长递增子序列问题
        if len(envelopes) == 0:
            return 0
        # 将list按第一个元素排序
        sort_list = sorted(envelopes,key=lambda item:(item[0],-item[1]))

        # dp[i]表示以nums[i]结尾的最长递增子序列
        dp = [1 for _ in range(len(sort_list))]
        for i in range(1,len(sort_list)):
            for j in range(i):
                if sort_list[j][1] < sort_list[i][1] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
        return max(dp)