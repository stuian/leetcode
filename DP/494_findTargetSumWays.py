class Solution:
    def findTargetSumWays(self, nums, S) :
        self.count = 0
        self.d = {}
        def dp(nums, row, rest):
            if row == len(nums):
                if rest == 0:
                    return 1
                else:
                    return 0
            if (row,rest) in self.d:
                return self.d[(row,rest)]
            self.d[(row,rest)] = dp(nums, row + 1, rest + nums[row]) + dp(nums, row + 1, rest - nums[row])
            return self.d[(row,rest)]

        if len(nums) == 0:
            return 0
        else:
            return dp(nums, 0, S)

def main():
    test = Solution()
    nums = [7, 46, 36, 49, 5, 34, 25, 39, 41, 38, 49, 47, 17, 11, 1, 41, 7, 16, 23, 13]
    S = 3
    result = test.findTargetSumWays(nums,S)
    print(result)

if __name__ == '__main__':
    main()