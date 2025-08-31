class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        #3 pointers approach kinda difficult to move which pointer but 
        #use when you dont know which pointer to move makes it easy that way
        hashmap = defaultdict(int)
        l= m = 0
        n = len(nums)
        res = 0
        for r in range(n):
            hashmap[nums[r]] += 1
            
            
            while len(hashmap) > k:
                hashmap[nums[m]] -= 1
                if hashmap[nums[m]] == 0:
                    del hashmap[nums[m]]
                m += 1
                l = m
                
            while hashmap[nums[m]] > 1:
                hashmap[nums[m]] -= 1
                m += 1
                
            if len(hashmap) == k:
                res += (m-l+1)
        return res


        # approach easy but not that intuitive
        # def helper(nums,k):
        #     l = 0
        #     n = len(nums)
        #     res = 0
        #     hashmap = defaultdict(int)
        #     for r in range(n):
        #         hashmap[nums[r]] += 1

        #         while len(hashmap) > k:
        #             # print(hashmap)
        #             hashmap[nums[l]] -= 1
        #             if hashmap[nums[l]] == 0:
        #                 del hashmap[nums[l]]
        #             l += 1

        #         if len(hashmap) <= k:
        #             res += r - l 
        #             # print(res)
        #     return res
        # return helper(nums,k) - helper(nums,k-1)