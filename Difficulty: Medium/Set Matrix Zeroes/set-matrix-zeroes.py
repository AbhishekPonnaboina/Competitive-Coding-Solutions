#User function Template for python3
class Solution:
    def setMatrixZeroes(self, mat):
        nr = len(mat)
        nc = len(mat[0])
        col0 = 1
        
        for i in range(nr):
            for j in range(nc):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    if j != 0:
                        mat[0][j] = 0
                    else:
                        col0 = 0
        for i in range(1,nr):
            for j in range(1,nc):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        
        if mat[0][0] == 0:
            for j in range(nc):
                mat[0][j] = 0
        
        if col0 == 0:
            for i in range(nr):
                mat[i][0] = 0
        