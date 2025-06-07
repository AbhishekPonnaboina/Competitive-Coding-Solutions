class Solution: 
    def selectionSort(self, arr , i = 0):
        #code here
        
        if i >= len(arr) - 1:
            return 
        
        small = i
        
        for j in range(i+1,len(arr)):
            if arr[small] > arr[j]:
                small = j
        
        arr[small],arr[i] = arr[i],arr[small]
        
        self.selectionSort(arr,i+1)
        
        
        """n = len(arr)
        
        for i in range(n - 1):
            small = i
            for j in range(i+1,n):
                if arr[small] > arr[j]:
                    small = j
            arr[small] ,arr[i] = arr[i] , arr[small]"""
        