class Solution:
    # Function to find all possible paths
    def ratInMaze(self, maze):
        # code here
        
        n = len(maze)
        
        res = []
        path = set()
        sub = ''
        
        def issafe(r,c):
            if r >= 0 and r < n and c >= 0 and c < n and maze[r][c] == 1 and (r,c) not in path:
                return True
            return False

        
        def solvemaze(sub,r,c):
            if r == n - 1 and c == n - 1:
                res.append(sub)
                return
            path.add((r,c))
            
            if issafe(r-1,c): ###solving for up
                # print("im here")
                sub += 'U'
                solvemaze(sub,r-1,c)
                sub = sub[:-1]
                
            if issafe(r,c+1): ###solving for right
                sub += 'R'
                # print("im here")
                solvemaze(sub,r,c+1)
                sub = sub[:-1]
                
            if issafe(r+1,c): ###solving for down
                sub += 'D'
                # print("im here")
                solvemaze(sub,r+1,c)
                sub = sub[:-1]
                
            if issafe(r,c-1): ###solving for left
                sub += 'L'
                # print("im here")
                solvemaze(sub,r,c-1)
                sub = sub[:-1]
            
            path.remove((r,c))
        
        solvemaze(sub,0,0)
        res.sort()
        return res
            
            