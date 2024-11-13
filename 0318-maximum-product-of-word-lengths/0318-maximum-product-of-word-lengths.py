class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        numrep = [0] * n
        maxa = 0

        for i in range(n):
            for ch in words[i] :
                numrep[i] |= 1 << (ord(ch) - 97)
            for j in range(i):
                if numrep[i] & numrep[j] == 0:
                    maxa = max(maxa,len(words[i])*len(words[j]))
        return maxa