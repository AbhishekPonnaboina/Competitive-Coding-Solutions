class Solution:
    def isPalindrome(self, s,a=0,b=None):
        # code here
        if not b:
            b = len(s)-1
        if a >= b:
            return True
        if s[a] != s[b]:
            return False
        return True and self.isPalindrome(s,a+1,b-1)
        
