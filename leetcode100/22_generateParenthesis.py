class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        def backtrack(s,left,right):
            if len(s) == 2*n:
                self.result.append("".join(s))
                return
            if left < n: # 左括号是可以一直加的
                s.append("(")
                backtrack(s,left+1,right)
                s.pop()
            if left > right:
                s.append(")")
                backtrack(s,left,right+1)
                s.pop()
        backtrack([],0,0)
        return self.result
