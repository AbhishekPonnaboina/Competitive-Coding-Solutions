class Solution:
    def countDigits(self, num: int) -> int:
        dup = num
        res = 0
        while dup:
            div = dup % 10
            if div == 0:
                break
            #print("div = ",div)
            if num % div == 0:
                res += 1
            dup //= 10
        return res