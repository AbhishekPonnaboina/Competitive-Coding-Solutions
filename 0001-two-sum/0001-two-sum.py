class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myhash = {}

        for i,j in enumerate(nums):
            if target - j in myhash:
                return [i,myhash[target-j]]
            myhash[j] = i