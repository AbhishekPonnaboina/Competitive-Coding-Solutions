class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        r,l = 0,0
        n = len(nums)
        res = 0
        hashmap = defaultdict(int)

        for r in range(n):
            hashmap[nums[r]] += 1
            # print("Hashmap before=",hashmap)
           
            while len(hashmap) > 2:
                hashmap[nums[l]] -= 1
                if hashmap[nums[l]] == 0:
                    del hashmap[nums[l]]
                l += 1
            # print("Hashmap After=",hashmap)
            res = max(res,r-l+1)
        return res   


  



        #wrote the brute force but it didnot work sad tle
        # r,l = 0,0
        # n = len(nums)
        
        # res = 0

        # for i in range(n):
        #     hashmap = defaultdict(int)
            
        #     for j in range(i,n):
        #         hashmap[nums[j]] += 1
        #         # print("hashmap",hashmap)
        #         if len(hashmap) > 2:
        #             break
        #         res = max(res,j-i+1)
        #     # print("------------------------")
        # return res
