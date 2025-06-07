class Solution:
    def findMin(self, arr: List[int]) -> int:
        res = float("infinity")
        low , high = 0, len(arr)-1

        while low <= high:
            mid = low + (high - low) // 2
            if arr[low] <= arr[mid]:
                res = min(res,arr[low])
                low = mid + 1
            else:
                res = min(res,arr[mid])
                high = mid - 1
        return res
