class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        low,high = 0,len(arr)-1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return True
            
            if arr[mid] == arr[low] == arr[high]:
                low += 1
                high -= 1
            
            elif arr[low] <= arr[mid]:
                if arr[low] <= target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1                       

            else:
                if arr[mid] < target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
