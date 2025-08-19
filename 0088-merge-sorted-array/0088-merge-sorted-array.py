class Solution:
    def merge(self, arr1: List[int], m: int, arr2: List[int], n: int) -> None:
        left = m - 1
        right = n - 1
        k = m + n - 1

        while left >= 0 and right >= 0:
            if arr1[left] > arr2[right] :
                arr1[k] = arr1[left]
                left -= 1            
            else:
                arr1[k] = arr2[right]
                right -= 1
            k -= 1
        
        while right >= 0:
            arr1[k] = arr2[right]
            k -= 1
            right -= 1

