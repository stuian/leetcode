class Solution:
    def findTargetSumWays(self, nums, S):
        self.count = 0
        def backtrack(n,nums,sol):
            if n == len(nums):
                if sol == S:
                    self.count += 1
                return
            for choose in [-1,1]:
                sol = sol + choose*nums[n]
                backtrack(n+1,nums,sol)
                sol = sol - choose*nums[n]
        backtrack(0,nums,0)
        return self.count

def main():
    test = Solution()
    nums = [7,46,36,49,5,34,25,39,41,38,49,47,17,11,1,41,7,16,23,13]
    S = 3
    result = test.findTargetSumWays(nums,S)
    print(result)

if __name__ == '__main__':
    main()