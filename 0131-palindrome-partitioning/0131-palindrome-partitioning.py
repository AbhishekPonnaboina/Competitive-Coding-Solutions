class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #just slight change to the backtracking similar pattern bro
        #should have it on your own but nvm
        def ispalindrome(stre,l,r):
            while l <= r:
                if stre[l] != stre[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        n = len(s)
        res = []
        sub = []
        def generatepalidrome(idx,s):
            if idx == n:
                res.append(sub.copy())
                return
            for i in range(idx,n):
                if ispalindrome(s,idx,i):
                    sub.append(s[idx:i+1])
                    generatepalidrome(i+1,s)
                    sub.pop()
        generatepalidrome(0,s)
        return res
