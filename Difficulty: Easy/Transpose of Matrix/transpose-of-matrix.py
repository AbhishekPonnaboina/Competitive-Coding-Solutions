#User function Template for python3

class Solution:
    def transpose(self, matrix, n):
        # Write Your code here
        n = len(matrix)
        temp = [[0 for _ in range(n)]for _ in range(n)]
        for i in range(n):
            for j in range(n):
                temp[i][j] = matrix[j][i]
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp[i][j]
        return matrix
        

#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
        
    ob = Solution()
    ob.transpose(matrix, n)
    
    for row in matrix:
        print(*row)
    
    print("~")
# } Driver Code Ends