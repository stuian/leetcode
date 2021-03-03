class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        m = len(num1)
        n = len(num2)
        res = [0 for _ in range(m + n)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                temp = numDict[num1[i]] * numDict[num2[j]]
                if temp // 10 == 0:  # 一位数
                    res[i + j + 1] += temp
                    if res[i + j + 1] // 10 != 0:
                        res[i + j] += res[i + j + 1] // 10
                        res[i + j + 1] = res[i + j + 1] % 10
                else:
                    res[i + j + 1] += temp % 10
                    if res[i + j + 1] // 10 != 0:
                        res[i + j] += res[i + j + 1] // 10
                        res[i + j + 1] = res[i + j + 1] % 10
                    res[i + j] += temp // 10
                    if res[i + j] // 10 != 0:
                        res[i + j - 1] += res[i + j] // 10
                        res[i + j] = res[i + j] % 10

        t = m + n - 1
        result = ""
        while t >= 0:
            result = str(res[t]) + result
            t -= 1
        while len(result) > 1:
            if result[0] == "0":
                result = result[1:]
            else:
                break
        return result


def main():
    test = Solution()
    result = test.multiply("45","123")
    print(result)

if __name__ == '__main__':
    main()