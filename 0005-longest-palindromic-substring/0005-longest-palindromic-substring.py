class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        res = "" 
        def plaindrome(left,right):
            while left >=  0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        for i in range(n):
            odd = plaindrome(i,i)
            if len(odd) > len(res):
                res = odd
            even = plaindrome(i,i+1)
            if len(even)> len(res):
                res = even
        return res
#this was all for generating every palindrome we can get from a string and itso(n^3) solution so trying to do better in the above approach
        # n = len(s)
        # if n == 1:
        #     return s

        # res = []

        # def ispalindrome(left,right):
            
        #     a = left
        #     b = right
        #     while left <= right:
        #         # print("sleft",s[left])
        #         # print("sright",s[right])
        #         if s[left] == s[right]:
        #             left += 1
        #             right -= 1
        #         else:
        #             return None
        #     else:
        #         # print("a",a)
        #         # print("b",b)
        #         return s[a:b+1]
            

        # for i in range(n):
        #     for j in range(n-1,i-1,-1):
        #         valid = ispalindrome(i,j)
        #         if valid:
        #             res.append(valid)
        #             break
        
        # str1 = max(res,key=len)
        # return str1

                        
