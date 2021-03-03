import collections
class Solution:
    def letterCombinations(self, digits):
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if digits == "":
            return []
        d = collections.deque([])
        d.append("")
        for i in range(len(digits)):
            for j in range(len(d)):
                pop_value = d.popleft()
                temp = dic[digits[i]]
                for t in range(len(temp)):
                    d.append(pop_value + temp[t])
        return list(d)

def main():
    test = Solution()
    result = test.letterCombinations("42")
    print(result)

if __name__ == '__main__':
    main()