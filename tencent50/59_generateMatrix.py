import numpy as np
class Solution:
    def generateMatrix(self, n):
        matrix = np.zeros((n,n),dtype=int)
        num = 0
        i = 0
        j = 0
        num += 1
        matrix[0][0] = num
        row = n
        col = n
        low_j = 0
        low_i = 1
        while num != n*n:
            while j < col-1:
                j += 1
                num += 1
                matrix[i][j] = num
                if num == n*n:
                    return matrix.tolist()
            while i < row-1:
                i += 1
                num += 1
                matrix[i][j] = num
                if num == n*n:
                    return matrix.tolist()
            while j > low_j:
                j -= 1
                num += 1
                matrix[i][j] = num
                if num == n*n:
                    return matrix.tolist()
            while i > low_i:
                i -= 1
                num += 1
                matrix[i][j] = num
                if num == n*n:
                    return matrix.tolist()
            low_i += 1
            low_j += 1
            row -= 1
            col -= 1
        return matrix.tolist()

def main():
    test = Solution()
    a = 1
    result = test.generateMatrix(a)
    print(result)

if __name__ == '__main__':
    main()