class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = list(map(lambda x : x * x , nums))
        a.sort()
        return a