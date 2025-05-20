from collections import Counter 
class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        cou = Counter(arr)
        res = 0
        
        
        for key,i in cou.items():
            if i > len(arr)//2:
                res = key
                
        return res