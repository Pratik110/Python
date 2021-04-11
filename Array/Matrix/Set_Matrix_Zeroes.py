Link = "https://leetcode.com/problems/set-matrix-zeroes/"
Description = "Given an m x n matrix. If an element is 0, set its entire row and column to 0"
Example = "https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg" \
          "Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]" \
          "Output: [[1,0,1],[0,0,0],[1,0,1]]"
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Approach 1, creating separate arrays for both Row and Columns and using them to store zeroes
# and form the resultant matrix by filling zeroes back in matrix

class Solution:
    def setZeroes(self,matrix):
        m = len(matrix)
        n = len(matrix[0])
        rowMatrix = [""]*m
        colMatrix = [""]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowMatrix[i] = 0
                    colMatrix[j] = 0
        for i in range(m):
            for j in range(n):
                if rowMatrix[i] == 0 or colMatrix[j] == 0:
                    matrix[i][j] = 0
        return matrix
print(Solution().setZeroes(matrix))
