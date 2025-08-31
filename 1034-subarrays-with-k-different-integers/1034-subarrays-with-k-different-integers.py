class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums,k):
            l = 0
            n = len(nums)
            res = 0
            hashmap = defaultdict(int)
            for r in range(n):
                hashmap[nums[r]] += 1

                while len(hashmap) > k:
                    # print(hashmap)
                    hashmap[nums[l]] -= 1
                    if hashmap[nums[l]] == 0:
                        del hashmap[nums[l]]
                    l += 1

                if len(hashmap) <= k:
                    res += r - l 
                    # print(res)
            return res
        return helper(nums,k) - helper(nums,k-1)