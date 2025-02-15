class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        lena = 0
        s = str(num)

        for i in range(k,len(s)+1):
            div = int(s[i-k:i])

            if div and num % div == 0:
                lena += 1
        return lena





        