class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        res = []

        for i in range(n):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            
            for j in range(i+1,n):
                if j > i+1 and arr[j] == arr[j-1]:
                    continue
                left = j + 1
                right = n - 1

                while left < right:
                    tot = arr[i]
                    tot += arr[j]

                    tot += arr[left] + arr[right]
                    
                    if tot == target:
                        res.append([arr[i],arr[j],arr[left],arr[right]])
                        left += 1
                        right -= 1

                        while left < right and arr[left] == arr[left-1]:
                            left += 1
                        while left < right and arr[right] == arr[right+1]:
                            right -= 1
                    
                    elif tot > target:
                        right -= 1
                    else:
                        left += 1
        return res














        # so here we are using the double set for storing and then also 
        # we are using another set for looking up the fourth value
        # n = len(nums)
        # myhash = set()

        # for i in range(n):
        #     for j in range(i+1,n):
        #         hashset = set()
        #         for k in range(j+1,n):
        #             suma = nums[i] + nums[j]
        #             suma += nums[k]
        #             fourth = target - (suma)
        #             if fourth in hashset:
        #                 temp = [nums[i],nums[j],nums[k],fourth]
        #                 temp.sort()
        #                 myhash.add(tuple(temp))
        #             hashset.add(nums[k])
        # print(myhash)
        # return list(myhash)
















        # basic approach
        # would be that o(n**4)


        
        