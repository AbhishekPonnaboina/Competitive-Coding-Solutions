class Solution: 
    def selectionSort(self, arr):
        #code here
        
        n = len(arr)
        
        for i in range(n - 1):
            small = i
            for j in range(i+1,n):
                if arr[small] > arr[j]:
                    small = j
            arr[small] ,arr[i] = arr[i] , arr[small]
        