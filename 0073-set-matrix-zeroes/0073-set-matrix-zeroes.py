class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        nr = len(matrix)
        nc = len(matrix[0])

        for i in range(nr):
            for j in range(nc):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0 

        for i in range(1,nr):
            for j in range(1,nc):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(nc):
                matrix[0][j] = 0
            
        if col0 == 0:
            for i in range(nr):
                matrix[i][0] = 0
            


        """nr = len(matrix)
        nc = len(matrix[0])
        rowidx = [0 for i in range(nr)]
        colidx = [0 for i in range(nc)]

        for i in range(nr):
            for j in range(nc):
                if matrix[i][j] == 0:
                    rowidx[i] = 1
                    colidx[j] = 1
        
        for i in range(nr):
            for j in range(nc):
                if rowidx[i] == 1 or colidx[j] == 1:
                    matrix[i][j] = 0"""
            
        
                                     
                                                                                   



