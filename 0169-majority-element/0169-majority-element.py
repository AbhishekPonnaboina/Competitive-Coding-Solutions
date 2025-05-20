from collections import Counter 
class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        #moore voting algorithm
        res = 0
        count = 1
        for i in range(1,len(arr)):
            if arr[res] == arr[i]:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                res = i
                count = 1
        return arr[res]






        """cou = Counter(arr)
        res = 0
        
        
        for key,i in cou.items():
            if i > len(arr)//2:
                res = key
                
        return res"""