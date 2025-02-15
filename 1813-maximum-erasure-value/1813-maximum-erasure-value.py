class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i = j = 0
        seen = set()
        ans = suma = 0

        for j in range(len(nums)):
            while nums[j] in seen:
                seen.remove(nums[i])
                suma-= nums[i]
                i += 1
            seen.add(nums[j])
            suma += nums[j]
            ans = max(ans,suma)

        return ans
            

        