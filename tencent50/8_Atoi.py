class Solution:
    def myAtoi(self, s: str) -> int:
        length = len(s)
        flag = 0
        start = 0
        if length == 0:
            return 0
        for i in range(length):
            if s[i] == " ":
                continue
            elif s[i] == "-":
                start = i+1
                flag = -1
                break
            elif s[i] == "+":
                start = i+1
                flag = 1
                break
            elif 48 <= ord(s[i]) <= 57:
                start = i
                flag = 1
                break
            else:
                return 0
        if flag == 0:
            return 0
        count = 0
        for j in range(start,length):
            if 48 <= ord(s[j]) <= 57:
                count += 1
            else:
                break
        num = 0
        for c in range(count):
            num += int(s[start+c]) * (10**(count-c-1))
        num = num*flag
        if num > 2**31-1:
            return 2**31-1
        elif num < -2**31:
            return -2**31
        else:
            return num

def main():
    test = Solution()
    result = test.myAtoi("42")
    print(result)

if __name__ == '__main__':
    main()