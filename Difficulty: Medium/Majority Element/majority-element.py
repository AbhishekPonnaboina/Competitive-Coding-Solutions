#User function template for Python 3
from collections import Counter
class Solution:
    def majorityElement(self, arr):
        #code here
    
        
        #MOORE VOTING ALGORRITHM
        
        res = 0
        count = 1
        
        for i in range(1,len(arr)):
            if arr[res] == arr[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                res = i
                count = 1
        count = 0
        for i in range(len(arr)):
            if arr[i] == arr[res]:
                count += 1
        if count > len(arr)//2 :
            return arr[res]
        return -1
        
                