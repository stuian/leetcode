import collections


class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        if len(s) % 2 != 0:
            return False
        d = collections.deque([])
        i = 0
        dic = {"(":")","[":"]","{":"}"}
        # Flag = 1
        while i < len(s):
            if len(d) == 0 and (s[i] == "(" or s[i] =="[" or s[i] =="{"):
                d.append(s[i])
                i += 1
            else:
                return False
            while len(d) != 0 and i < len(s):
                string = d.pop()
                if s[i] != dic[string] and (s[i] == "(" or s[i] =="[" or s[i] =="{"):
                    d.append(string)
                    d.append(s[i])
                    i += 1
                elif s[i] == dic[string]:
                    i += 1
                else:
                    return False
            if len(d) != 0:
                return False
        return True

def main():
    test = Solution()
    result = test.isValid("((")
    print(result)

if __name__ == '__main__':
    main()