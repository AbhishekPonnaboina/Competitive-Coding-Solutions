#User function Template for python3

class Solution:
    def Search(self, arr, key):
        # code here
        low , high = 0 , len(arr) - 1
        
        while low <= high:
            mid = low + (high - low ) // 2
            if arr[mid] == key:
                return True
            if arr[mid] == arr[low]:
                low += 1
                continue
            if arr[mid] == arr[high]:
                high -= 1
                continue
            
            if arr[low] <= arr[mid]:
                if arr[low] <= key < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if arr[mid] < key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False