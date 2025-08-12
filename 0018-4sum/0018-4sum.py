class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        myhash = set()

        for i in range(n):
            for j in range(i+1,n):
                hashset = set()
                for k in range(j+1,n):
                    suma = nums[i] + nums[j]
                    suma += nums[k]
                    fourth = target - (suma)
                    if fourth in hashset:
                        temp = [nums[i],nums[j],nums[k],fourth]
                        temp.sort()
                        myhash.add(tuple(temp))
                    hashset.add(nums[k])
        
        return list(myhash)
















        # basic approach
        # would be that o(n**4)


        
        