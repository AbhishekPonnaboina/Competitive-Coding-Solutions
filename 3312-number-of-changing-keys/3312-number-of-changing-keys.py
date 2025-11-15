class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        a = s[0]
        res = 0

        for i in s:
            if i.lower() != a.lower():
                a = i
                res += 1
        
        return res