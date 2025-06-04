from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        myhash = Counter(s)
        res = 0
        has_odd = False
        for k,v in myhash.items():
            #print(v)
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                has_odd = True
        if has_odd:
            return res + 1
        return res

        