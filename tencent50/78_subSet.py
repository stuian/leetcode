class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res
def main():
    test = Solution()
    a = [1,2,3]
    result = test.subsets(a)
    print(result)

if __name__ == '__main__':
    main()