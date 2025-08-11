

class Solution:
    def triplets(self, arr ):
        # code here\
        arr.sort()
        res = []
        
        
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            val = arr[i]
            left = i + 1
            right = len(arr) - 1
            
            while left < right:
                tot = val + arr[left] + arr[right]
                
                if tot == 0:
                    res.append([val,arr[left],arr[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and arr[left] == arr[left-1]:
                        left += 1
                    while left < right and arr[right] == arr[right+1]:
                        right -= 1
                elif tot > 0:
                    right -= 1
                else:
                    left += 1
            
        return res
