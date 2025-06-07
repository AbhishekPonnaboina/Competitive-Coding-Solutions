class Solution:
    def mergesubarrays(self,arr,low,mid,high):
        left = arr[low:mid+1]
        right = arr[mid+1:high+1]
        i,j = 0,0
        k = low
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
 
    def mergeSort(self,arr, l, r):
        #code here
        if r > l:
            mid = (l + r) // 2
            self.mergeSort(arr,l,mid)
            self.mergeSort(arr,mid+1,r)
            self.mergesubarrays(arr,l,mid,r)
        return arr
    