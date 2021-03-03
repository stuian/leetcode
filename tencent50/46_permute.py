import collections
class Solution:
    def permute(self, nums):
        if len(nums) <= 1:
            return nums
        d = collections.deque([])
        for i in range(len(nums)):
            d.append([nums[i]])
        for i in range(1,len(nums)):
            for j in range(len(d)):
                pop_value = d.popleft()
                for p in nums:
                    temp = list(pop_value)
                    if p not in temp:
                        temp.append(p)
                        d.append(temp)
        return list(d)

def main():
    test = Solution()
    result = test.permute([1,2,3])
    print(result)

if __name__ == '__main__':
    main()