class Solution:
    def findMaxConsecutiveOnes(self, arr: List[int]) -> int:
        
        res = 0
        left = 0
        right = 0

        while right < len(arr):
            if  arr[right] == 1:
                right += 1
            else:
                res = max(res,right-left)
                left = right + 1
                right += 1
        res = max(res, right - left)
        return res