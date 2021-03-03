# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1 :
#             return 1
#         if n == 2:
#             return 2
#         return self.climbStairs(n-2) + self.climbStairs(n-1)

# 递归太慢了，竟然超时了

class Solution:
    # 空间换时间，动态规划
    def climbStairs(self, n: int) -> int:
        climb = {}

        climb[0] = 0
        climb[1] = 1
        climb[2] = 2

        for i in range(3, n + 1):
            climb[i] = climb[i - 1] + climb[i - 2]
        return climb[n]

def main():
    test = Solution()
    a = 38
    result = test.climbStairs(a)
    print(result)

if __name__ == '__main__':
    main()