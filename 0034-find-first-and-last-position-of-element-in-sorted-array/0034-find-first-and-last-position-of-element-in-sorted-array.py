class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        n = len(arr)
        first = -1
        last = -1

        low,high = 0 , n - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                first = mid
                high = mid - 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
            
        low,high = 0 , n - 1

        while low <= high:
            mid = (low + high )//2
            if arr[mid] == target:
                last = mid
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
            
        
        return [first,last ]
        
    