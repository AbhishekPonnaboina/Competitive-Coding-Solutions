class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []
        #here we need to do the simple at each step do we add the element or not 
        #like include the element or not include the element thats it 
        def BackTracking(i):
            if i >= n:
                print(subset)
                res.append(subset.copy())
                return
            #incluind the current index element
            subset.append(nums[i])
            BackTracking(i+1)

            #Here not including the element 
            #so we just need to remove the element we added
            subset.pop()
            BackTracking(i+1)
        
        BackTracking(0)
        return res

        #Bit manipulation approach
        # subsets = 2 ** len(nums)
        # res = [[]for _ in range(subsets)]
        

        # for i in range(0,subsets):
        #     vala = []
        #     for j in range(len(nums)):
        #         x = i & (1 << j)
        #         if x:
        #             vala.append(nums[j])
        #     res[i] = vala
        
        # return res