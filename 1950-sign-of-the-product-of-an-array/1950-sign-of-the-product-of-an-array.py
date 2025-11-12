class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = reduce(lambda x,y: x*y,nums)

        if ans > 0:
            return 1
        elif ans < 0:
            return -1
        else:
            return 0     