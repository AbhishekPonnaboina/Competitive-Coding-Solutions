class Solution:
    def findErrorNums(self, arr: List[int]) -> List[int]:

        #solved on gfg firstu then here
        n = len(arr)
        xor = 0
        
        for i in range(n):
            xor ^= arr[i]
            xor ^= i+1
        
        #settedBIt the right most set bit for grouping into two
        bit = xor & ~(xor - 1)
        
        zeros = 0 #forming a group of numbers whos numbers are setted as 0
        ones = 0 #forming a group of numbers whos numbers are setted as 1
        
        for i in range(n):
            if (arr[i] & bit) == 0:
                zeros ^= arr[i]
                
            else:
                ones ^= arr[i]
        
        for i in range(1,n+1):
            if (i & bit) == 0:
                zeros ^= i
                
            else:
                ones ^= i
        
        for val in arr:
            if val == zeros:
                return [zeros,ones]
        
        return [ones,zeros]
                
        # n = len(arr)
        # sum1 = 0 
        # sum2 = 0
        
        # a = (n * (n+1)) // 2
        # b = (n * (n+1) *(2*n+1)) // 6
        
        # for i in range(n):
        #     sum1 += arr[i]
        #     sum2 += arr[i] * arr[i]
            
        
        # val1 = sum1 - a
        # val2 = sum2 - b
        # val2 = val2 // val1
        
        # x = (val1 + val2) // 2 
        # y =  x - val1
        
        # return [x,y]