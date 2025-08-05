class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = 2 ** len(nums)
        res = [[]for _ in range(subsets)]
        

        for i in range(0,subsets):
            vala = []
            for j in range(len(nums)):
                x = i & (1 << j)
                if x:
                    vala.append(nums[j])
            res[i] = vala
        
        return res
        