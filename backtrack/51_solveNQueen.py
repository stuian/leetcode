class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        check = [["."]*n for _ in range(n)]
        self.res = []
        def isValid(check,row,col): # 剪枝
            n = len(check)
            # 检查列是否有皇后冲突
            for i in range(n):
                if check[i][col] == "Q":
                    return False
            # 检查左上方是否有皇后冲突
            for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
                if check[i][j] == "Q":
                    return False
            # 检查右上方是否有皇后冲突
            for i,j in zip(range(row,-1,-1),range(col,n)):
                if check[i][j] == "Q":
                    return False
            return True

        def backtrack(row,check):
            if row == len(check):
                p = []
                for i in range(n):
                    p.append(''.join(check[i]))
                self.res.append(p)
                return
            for col in range(len(check)): # col
                if not isValid(check,row,col):
                    continue
                check[row][col] = "Q"
                backtrack(row+1,check)
                check[row][col] = "."
        backtrack(0,check)
        return self.res