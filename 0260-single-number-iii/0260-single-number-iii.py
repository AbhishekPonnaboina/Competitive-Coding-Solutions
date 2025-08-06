class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        myxor = 0

        for i in nums:
            myxor ^= i
        
        bit = (myxor & myxor - 1) ^ myxor

        ones,twos = 0,0

        for i in nums:
            if bit & i:
                ones ^= i
            else:
                twos ^= i
        return [ones,twos]