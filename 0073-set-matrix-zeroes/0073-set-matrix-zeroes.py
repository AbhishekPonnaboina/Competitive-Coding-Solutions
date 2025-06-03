class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nr = len(matrix)
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
                    matrix[i][j] = 0
            
        
                                     
                                                                                   



