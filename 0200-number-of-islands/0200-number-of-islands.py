class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(grid,i,j):
            

            if (i < 0 or i > row-1 or j < 0 or j > col-1 or grid[i][j] != '1'):
                return 
                
            grid[i][j] = '2'

            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
            dfs(grid,i-1,j)
            dfs(grid,i+1,j)         
           
            


        counta = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    counta += 1
                    dfs(grid,i,j)

        return counta




        