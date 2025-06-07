class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        # code here
        
        n = len(arr) - 1
        
        for i in range(n):
            for j in range(n-i):
                if arr[j] > arr[j+1]:
                    arr[j] , arr[j+1] = arr[j+1],arr[j]
    
        