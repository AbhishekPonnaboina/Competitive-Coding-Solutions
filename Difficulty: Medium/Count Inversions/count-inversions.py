class Solution:
    def inversionCount(self, arr):
        # Code Here 
        def mergesort(low,high):
            if low >= high:
                return
            mid = (low+ high) // 2
            mergesort(low,mid)
            mergesort(mid+1,high)
            mergearray(low,mid,high)
        
        def mergearray(low,mid,high):
            left = low
            right = mid + 1
            temp = []
            
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    inversions[0] += mid - left + 1
                    right += 1
            while left <= mid:
                temp.append(arr[left])
                left += 1
            while right <= high:
                temp.append(arr[right])
                right += 1
            
            for i in range(len(temp)):
                arr[low + i] = temp[i]
            
        inversions = [0]
        n = len(arr) - 1
        mergesort(0,n)
        return inversions[0]
        
            
                    
                    
            