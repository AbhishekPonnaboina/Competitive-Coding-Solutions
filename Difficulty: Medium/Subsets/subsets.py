#User function Template for python3

class Solution:
    def subsets(self, arr):
        # code here
        subsets = 2 ** len(arr)
        res = [[]for _ in range(subsets)]
        
        for i in range(subsets):
            val = []
            for j in range(len(arr)):
                if i & 1 << j:
                    val.append(arr[j])
            res[i]=val
        
        res = sorted(res)
        return res