class Solution:
    def rob(self, nums):
        if nums == []:
            return 0
        self.res = 0
        check = [0 for _ in range(len(nums))]
        def backtrack(sol,nums,check):
            if check[len(nums)-2] == 1 or check[len(nums)-1] == 1:
                temp = sum(sol)
                if temp > self.res:
                    self.res = temp
                return
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if (i> 0 and check[i-1]==1) or (i+1<len(nums) and check[i+1]==1):
                    continue
                check[i] = 1
                backtrack(sol+[nums[i]],nums,check)
                check[i] = 0
        backtrack([],nums,check)
        return self.res

def main():
    test = Solution()
    result = test.rob([1,2,3,1])
    print(result)

if __name__ == '__main__':
    main()