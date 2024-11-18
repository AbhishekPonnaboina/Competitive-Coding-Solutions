
#User function Template for python3

class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
       # code here 
       row = len(matrix)
       col = len(matrix[0])
       res = []
       
       for i in range(row):
            if i % 2 == 0:
                for j in range(col):
                   res.append(matrix[i][j])
            else:
                for j in range(col-1,-1,-1):
                    res.append(matrix[i][j])
       
       
       return res
       
       
       


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.snakePattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


        print("~")
# } Driver Code Ends