class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr,n = None):
        # code here
        if n == None:
            n = len(arr)
        
        if n == 1:
            return 
        
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i] , arr[i+1] = arr[i+1] , arr[i]
        
        
        
        self.bubbleSort(arr,n-1)
        
        
        
        
        
        
        
        
        """n = len(arr) - 1
        
        for i in range(n):
            Flag = False
            for j in range(n-i):
                Flag = True
                if arr[j] > arr[j+1]:
                    arr[j] , arr[j+1] = arr[j+1],arr[j]
            if Flag == False:
                return """
        