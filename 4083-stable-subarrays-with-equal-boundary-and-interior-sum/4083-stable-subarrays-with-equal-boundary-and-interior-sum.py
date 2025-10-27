from collections import defaultdict
class Solution:
    def countStableSubarrays(self, arr: list[int]) -> int:
        """
         # here comes the main prefix part actaully the formula for 
            # prefix calculation is that sum(l...r) = prefix[r] - prefix[l-1] this gives sum from the l ... r
            # but here we are trying not to include the r and l indexes 
            # this is a custom prefix hashmap lookup accounting to three values being same
            # okay and also this [0,0,0] or [0,0,0,0] this is was the main problem 
            #but using left pointer with -2 gonna do the work 
            # this way we only start from the 2 
            # annd check correct values which was the main issue from earlier
        """

        n = len(arr)
        prefix = [0] * (n+1)

        for i,x in enumerate(arr):
            prefix[i]= prefix[i-1] + x
        # print(*prefix)
        ans = 0
        hashmap = {}

        for r in range(2,n):
            l = r - 2
            # print("key=",(arr[l],prefix[l]))
            # print("val=",hashmap.get((arr[l],prefix[l]),0)+1)
            hashmap[(arr[l],prefix[l])] = hashmap.get((arr[l],prefix[l]),0) + 1
            # print("key we are looking for =",arr[r])
            # print("the prefix we are looking for =",prefix[r-1]-arr[r])

           
            ans += hashmap.get((arr[r],prefix[r-1] - arr[r]),0)
        return ans




        #this is not working when prefix becomes zero fuck this approach
        # n = len(arr)
        # hashmap = defaultdict(lambda : defaultdict(int))
        # presum = 0
        # ans = 0

        # for i in range(n):
        #     if i >= 2 and arr[i] in hashmap:
        #         sub = hashmap[arr[i]]
        #         ans += sub.get(presum - arr[i], 0)
        #         print("yay")
        #     presum += arr[i]
        #     hashmap[arr[i]][presum] += 1
        #     # print("first hashmp=",*hashmap ,"hashmapvalues=",hashmap[arr[i]])
        #     print(hashmap)

        # # print(hashmap)


        # return ans


        


        
        #this also didnt work because there is a better way to do
        # this is o(n**2) and o(n) space
        # n = len(arr)
        # res = 0
        # prefixarr = [0]*n
        
        # prefixarr[0] = arr[0]
        # for i in range(1,n):
        #     prefixarr[i] = prefixarr[i-1] + arr[i]

        # for i in range(n-2):
        #     for j in range(i+2,n):
                
        #         if arr[i] == arr[j]:
        #             if prefixarr[j-1] - prefixarr[i] == arr[i]:
        #                 res += 1
                    
                    
        # return res


        # n * 3 not working proababy need the prefix array
        # res = 0
        # n = len(arr)


        # for i in range(n):
        #     for j in range(i+2,n):
        #         if arr[i] == arr[j] :
        #             suma = sum(arr[i+1:j])
        #             if arr[i] == suma:
        #                 res += 1

        # return res