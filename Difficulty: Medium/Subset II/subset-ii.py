#User function Template for python3

class Solution:
    def printUniqueSubset(self, arr):
        # Code here
        arr.sort()
        res = []
        sub = []
        n = len(arr)
        
        def generateSubSets(arr,res,sub,idx,n):
            res.append(sub.copy())
            for i in range(idx,n):
                if i > idx and arr[i] == arr[i-1]:
                    continue
                sub.append(arr[i])
                generateSubSets(arr,res,sub,i+1,n)
                sub.pop()
        
        generateSubSets(arr,res,sub,0,n)
        
        return res