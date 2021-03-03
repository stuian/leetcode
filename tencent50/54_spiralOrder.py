class Solution:
    def spiralOrder(self, matrix):
        if matrix == [[]] or matrix == []:
            return matrix
        num = 0
        i = 0
        j = 0
        output = []
        output.append(matrix[0][0])
        num += 1
        m = len(matrix)
        n = len(matrix[0])
        row = m
        col = n
        low_j = 0
        low_i = 1
        while num != m*n:
            while j < col-1:
                j += 1
                output.append(matrix[i][j])
                num += 1
                if num == m*n:
                    return output
            while i < row-1:
                i += 1
                output.append(matrix[i][j])
                num += 1
                if num == m*n:
                    return output
            while j > low_j:
                j -= 1
                output.append(matrix[i][j])
                num += 1
                if num == m*n:
                    return output
            while i > low_i:
                i -= 1
                output.append(matrix[i][j])
                num += 1
                if num == m*n:
                    return output
            low_i += 1
            low_j += 1
            row -= 1
            col -= 1
        return output


def main():
    test = Solution()
    a = []
    result = test.spiralOrder(a)
    print(result)

if __name__ == '__main__':
    main()