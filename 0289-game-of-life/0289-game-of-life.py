class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def livecnt(i,j,board):
            live = 0
            if i-1 >=0  and j-1 >=0 and board[i-1][j-1] == 1:
                live += 1

            if i-1 >= 0 and board[i-1][j] == 1:
                live += 1
            if i-1>=0 and j+1 < nc and board[i-1][j+1] == 1:
                live += 1
            if j-1 >= 0 and board[i][j-1] == 1:
                live += 1
            if j+1 < nc and board[i][j+1] == 1:
                live += 1
            if i+1 < nr and j-1 >= 0 and board[i+1][j-1] == 1:
                live += 1
            if i+1 < nr and board[i+1][j] == 1:
                live += 1
            if i+1 < nr and j+1 < nc and board[i+1][j+1] == 1:
                live += 1

            return live

        nr = len(board)
        nc = len(board[0])
        dup = [[0]*nc for _ in range(nr)]

        for i in range(nr):
            for j in range(nc):
                dup[i][j] = board[i][j]

        for i in range(nr):
            for j in range(nc):
                live  = livecnt(i,j,dup)
                if dup[i][j] == 1:                    
                    if live == 2 or live == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                else:
                    if live == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0