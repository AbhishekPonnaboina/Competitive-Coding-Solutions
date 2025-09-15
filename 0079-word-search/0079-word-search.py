class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #struggled with base case so watched the video now i think you wont struggle nexttime
        #just classic problem 
        #o(m*n) for board traversal so 6*6
        #o(4*len(word)) that is 4*15
        # so that totaltime complexity
        # and utmost o(16) in space so constant

        rows = len(board)
        cols = len(board[0])
        n = len(word)

        path = set()

        def dfs(r,c,i):
            if i == n:
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i] or (r,c) in path:
                return False
            
            path.add((r,c))
            res = (
                    dfs(r-1,c,i+1) or
                    dfs(r,c+1,i+1) or
                    dfs(r+1,c,i+1) or
                    dfs(r,c-1,i+1)
                )
            path.remove((r,c))
            
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False

        




