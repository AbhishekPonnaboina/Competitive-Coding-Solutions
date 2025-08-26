class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        res = []

        def ispalindrome(left,right):
            
            a = left
            b = right
            while left <= right:
                # print("sleft",s[left])
                # print("sright",s[right])
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return None
            else:
                # print("a",a)
                # print("b",b)
                return s[i:j+1]
            

        for i in range(n):
            for j in range(n-1,i-1,-1):
                valid = ispalindrome(i,j)
                if valid:
                    res.append(valid)
                    break
        
        str1 = max(res,key=len)
        return str1

                        
