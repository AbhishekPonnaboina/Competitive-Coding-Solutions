class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        counta = 0
        lena = len(s)
        for i in range((lena - 3) + 1 ):
            sub = s[i:i+3]
            if len(set(sub)) == 3:
                counta += 1
        return counta

            