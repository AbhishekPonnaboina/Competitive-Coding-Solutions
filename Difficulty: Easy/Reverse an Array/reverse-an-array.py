class Solution:
    def reverseArray(self, arr,a=0,b=None):
        # code here
        if not b:
            b = len(arr)-1
        if a >= b:
            return 
        arr[a],arr[b] = arr[b],arr[a]
        self.reverseArray(arr,a+1,b-1)
        
        