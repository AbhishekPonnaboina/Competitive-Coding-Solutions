#User function Template for python3

class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        # code here 
        row = n
        c = m
        res = []
        
        if row == 1:
            for i in range(c):
                res.append(matrix[0][i])
        
                
        elif c == 1:
            for i in range(row):
                res.append(matrix[i][0])
        else:
            for i in range(c):
                res.append(matrix[0][i])
                
            for i in range(1,row):
            
                res.append(matrix[i][c-1])
            
            if row > 1:
                for i in range(c-2,-1,-1):
                    res.append(matrix[row-1][i])
            
            if c > 1:
                for i in range(row-2,0,-1):
                    res.append(matrix[i][0])
        return res
                
                
                
                
                
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

        print("~")
# } Driver Code Ends