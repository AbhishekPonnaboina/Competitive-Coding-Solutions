class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ### used hashing to lookup for queen attacking places very nice trick to look up for diagonals and rows and other things bro
        #learned alot from this whole one problem
        rows = n
        cols = n
        res = []
        board = [["." for _ in range(cols)]for _ in range(rows)]
        upperdiagonal = [0 for _ in range(2*n - 1)]
        lowerdiagonal = [0 for _ in range(2*n - 1)]
        rowcheck = [0 for _ in range(rows)]

        def solve(c):
            if c == n:
                res.append(["".join(r) for r in board])
                return
            
            for r in range(n):
                if (rowcheck[r] == 0 and upperdiagonal[r+c] == 0 and lowerdiagonal[n-1 + (c - r)] == 0):
                    rowcheck[r] = 1
                    upperdiagonal[r+c] = 1
                    lowerdiagonal[n-1 + (c-r)] = 1
                    board[r][c] = 'Q'
                    solve(c+1)
                    board[r][c] = '.'
                    rowcheck[r] = 0
                    upperdiagonal[r+c] = 0
                    lowerdiagonal[n-1 + (c-r)] = 0
        solve(0)
        return res


        
        
        # ##this is o(n^3) approach but we do have o (n*n) abopve
        
        # rows = n
        # cols = n
        # res = [] #not one combination all the combinations

        # board = [["." for _ in range(cols)]for _ in range(rows)]

        # # one way of creating the board
        # # for r in range(rows):
        # #     row = []
        # #     for c in range(cols):
        # #         row.append(".")
        # #     board.append(row)

        # def isSafeToPlace(r,c):
        #     duprow = r
        #     dupcol = c
        #     # <- checking in this direction row same col different

        #     while dupcol >= 0:
        #         if board[duprow][dupcol] == 'Q':
        #             return False
        #         dupcol -= 1
            
        #     duprow = r
        #     dupcol = c

        #     while duprow >= 0 and dupcol >= 0:
        #         if board[duprow][dupcol] == 'Q':
        #             return False
        #         dupcol -= 1
        #         duprow -= 1
            
        #     duprow = r
        #     dupcol = c
            
        #     while duprow < n and dupcol >= 0:
        #         if board[duprow][dupcol] == 'Q':
        #             return False
        #         dupcol -= 1
        #         duprow += 1
            
        #     return True


        # def solve(c):
        #     if c == n:
        #         res.append(["".join for r in board])
        #         return

        #     for r in range(n):
        #         if isSafeToPlace(r,c):
        #             board[r][c] = 'Q'
        #             solve(c+1)
        #             board[r][c] = '.'
        
        # solve(0)

        # return res 
