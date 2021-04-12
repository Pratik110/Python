Link = "https://leetcode.com/problems/rotate-image/"
Description = "You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise)." \
              "You have to rotate the image in-place, which means you have to modify the input 2D matrix directly." \
              "DO NOT allocate another 2D matrix and do the rotation."
Example = "Input: matrix = [[1,2,3]," \
          "                 [4,5,6]," \
          "                 [7,8,9]]" \
          "" \
          "Output:         [[7,4,1]," \
          "                 [8,5,2]," \
          "                 [9,6,3]]"

# Approach 1
# We're going to first transpose the matrix then flip it, that'll get the job done.

class Solution1:
    def rotate(self,matrix):
        # Step 1 : Transpose the matrix
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(i,c):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp #instead of going through the traditional method of swapping, we can simply do
                                    #matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j], i.e, a,b = b,a
        # Step 2 : Flip the matrix
        for i in range(r):
            for j in range(c//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][c-j-1]
                matrix[i][c - j - 1] = temp

        return matrix



matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(Solution1().rotate(matrix))
