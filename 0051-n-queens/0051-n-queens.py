class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        rows = n
        cols = n
        res = [] #not one combination all the combinations

        board = [["." for _ in range(cols)]for _ in range(rows)]

        # one way of creating the board
        # for r in range(rows):
        #     row = []
        #     for c in range(cols):
        #         row.append(".")
        #     board.append(row)

        def isSafeToPlace(r,c):
            duprow = r
            dupcol = c
            # <- checking in this direction row same col different

            while dupcol >= 0:
                if board[duprow][dupcol] == 'Q':
                    return False
                dupcol -= 1
            
            duprow = r
            dupcol = c

            while duprow >= 0 and dupcol >= 0:
                if board[duprow][dupcol] == 'Q':
                    return False
                dupcol -= 1
                duprow -= 1
            
            duprow = r
            dupcol = c
            
            while duprow < n and dupcol >= 0:
                if board[duprow][dupcol] == 'Q':
                    return False
                dupcol -= 1
                duprow += 1
            
            return True


        def solve(c):
            if c == n:
                res.append(["".join(r) for r in board])
                return

            for r in range(n):
                if isSafeToPlace(r,c):
                    board[r][c] = 'Q'
                    solve(c+1)
                    board[r][c] = '.'
        
        solve(0)

        return res 
