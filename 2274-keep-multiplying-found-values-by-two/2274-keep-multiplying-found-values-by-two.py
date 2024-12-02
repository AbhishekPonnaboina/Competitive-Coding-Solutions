class Solution:
    def findFinalValue(self, arr: List[int], original: int) -> int:
        res = original
        for i in range(len(arr)):
            if original in arr:
                res = 2 * original
                original = res
        return res