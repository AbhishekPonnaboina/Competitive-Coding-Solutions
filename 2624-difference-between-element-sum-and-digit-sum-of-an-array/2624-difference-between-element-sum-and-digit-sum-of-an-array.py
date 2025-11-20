class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        suma = 0
        ela = 0

        for i in nums:
            suma += i
            while i:
                ela += i % 10
                i //= 10
        
        return  abs(ela - suma)