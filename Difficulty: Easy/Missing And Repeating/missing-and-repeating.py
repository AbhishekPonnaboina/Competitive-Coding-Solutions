class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)
        sum1 = 0 
        sum2 = 0
        
        a = (n * (n+1)) // 2
        b = (n * (n+1) *(2*n+1)) // 6
        
        for i in range(n):
            sum1 += arr[i]
            sum2 += arr[i] * arr[i]
            
        
        val1 = sum1 - a
        val2 = sum2 - b
        val2 = val2 // val1
        
        x = (val1 + val2) // 2 
        y =  x - val1
        
        return [x,y]
        

