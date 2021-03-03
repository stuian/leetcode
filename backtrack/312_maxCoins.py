class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #回溯法，穷举
        # 可选择的气球
        self.maxcoins = float("-inf")
        def backtrack(nums,result,choice):
            if 0 not in choice:
                if result > self.maxcoins:
                    self.maxcoins = result
                return
            for i in range(len(nums)):
                if choice[i] == 0:
                    choice[i] = 1
                    pre = 1
                    post = 1
                    for p in range(i-1,-1,-1):
                        if choice[p] == 0:
                            pre = nums[p]
                            break
                    for q in range(i+1,len(nums)):
                        if choice[q] == 0:
                            post = nums[q]
                            break
                    backtrack(nums,result + pre*nums[i]*post,choice)
                    choice[i] = 0
        choice = [0 for _ in range(len(nums))]
        backtrack(nums,0,choice)
        return self.maxcoins

