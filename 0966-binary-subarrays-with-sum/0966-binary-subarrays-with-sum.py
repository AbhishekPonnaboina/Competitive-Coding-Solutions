class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #optimal approach were we count the subaarays in a crazy way 
        #refer to book

        def helper(nums,goal):
            if goal < 0:
                return 0
            r,l = 0,0
            n = len(nums)
            suma = 0
            c = 0
            while r < n:
                suma += nums[r]

                while suma > goal:
                    suma -= nums[l]
                    l += 1
                c += r - l +1
                r += 1
            return c
        
        return helper(nums,goal) - helper(nums,goal-1)







        #brute force not worked we do have the btter approach with hashing 
        # that is similar to count the subarrays which equal sum = k
        # res = 0
        n = len(nums)
        res = 0
        for i in range(n):
            suma = 0
            for j in range(i,n):
                suma += nums[j]
                if suma == goal:
                    res += 1
                if suma > goal:
                    break
        # print(res)
        return (res)
        