class Solution:
    def reverseWords(self, s: str) -> str:
        seg = s.split(" ")
        temp = ""
        for index,st in enumerate(seg):
            string = []
            for i in range(len(st)):
                string.append(st[i])
            length = len(string)
            half_length = length // 2
            for i in range(half_length):
                a = string[i]
                string[i] = string[length-1-i]
                string[length-1-i] = a
            temp += "".join(string)
            if index != len(seg)-1:
                temp += " "
        return temp

def main():
    test = Solution()
    a = "Let's take LeetCode contest"
    print(test.reverseWords(a))

if __name__ == '__main__':
    main()