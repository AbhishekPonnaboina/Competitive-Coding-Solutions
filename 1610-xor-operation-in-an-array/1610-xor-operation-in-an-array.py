class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        # num = [0]*n

        for i in range(n):
            num = start + (2 * i)
            ans ^= num
        # print(*num)
        return ans