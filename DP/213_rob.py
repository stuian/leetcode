class Solution:
    def rob(self, nums):
        if nums == []:
            return 0
        dp = nums.copy()
        if len(nums) <= 2:
            return max(nums)
        temp = []
        temp.append(0)
        for i in range(2,len(nums)):
            if i == len(nums)-1:
                if i-1 > 1:
                    t = float("-inf")
                    for j in range(1,i-1):
                        if j not in temp and dp[j]>t:
                            t = dp[j]
                    dp[i] += t # 最后一个节点不能选包含第一个节点的
            else:
                t = float("-inf")
                for j in range(i-1):
                    if dp[j] > t:
                        t = dp[j]
                        index = j
                dp[i] += t
                if index in temp:
                    temp.append(i)
        return max(dp)

def main():
    test = Solution()
    result = test.rob([6,6,4,8,4,3,3,10])
    print(result)

if __name__ == '__main__':
    main()