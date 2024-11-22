class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        res = s[0]

        count = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            
            if count < 3:
                res += s[i]    
                
            
        return res

                
