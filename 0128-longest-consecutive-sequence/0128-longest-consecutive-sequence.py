class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        res = 0
        for val in arr:
            if val - 1 not in arr:
                maxi = 1
                currnum = val

                while currnum + 1 in arr:
                    maxi += 1
                    currnum += 1
                
                res = max(res,maxi)
        return res 
            