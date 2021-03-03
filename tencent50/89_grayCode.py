class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        res = [0]
        for i in range(n):
            a = list(reversed(res))
            res = res + [j+2**i for j in a]
        return res


def main():
    test = Solution()
    a = 3
    result = test.grayCode(a)
    print(result)

if __name__ == '__main__':
    main()