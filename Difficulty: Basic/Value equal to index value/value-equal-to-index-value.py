#User function Template for python3
class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        res = []
        for i,val in enumerate(arr):
            if i+1 == val:
                res.append(val)
        return res