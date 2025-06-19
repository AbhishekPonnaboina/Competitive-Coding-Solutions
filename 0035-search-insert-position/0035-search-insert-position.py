class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        low = 0
        high = len(arr) - 1
        res = len(arr)

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res