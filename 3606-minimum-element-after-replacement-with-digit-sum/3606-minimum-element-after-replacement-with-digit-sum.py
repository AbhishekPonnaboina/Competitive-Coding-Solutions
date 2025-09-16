class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        def helper(num):
            suma = 0
            while num > 0:
                suma += num % 10
                num //= 10
            return suma

        for i in range(n):
            nums[i] = helper(nums[i])

        return min(nums) 