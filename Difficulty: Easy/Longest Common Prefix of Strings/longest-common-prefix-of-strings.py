#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        res = ''
        arr.sort()
        
        for i in range(len(arr[0])):
            if arr[0][i] != arr[-1][i]:
                break
            res += arr[0][i]
        return res