class Solution:
    def countStableSubarrays(self, capacity: list[int]) -> int:
        n = len(capacity)
        prefix = [0]*(n+1)
        for i, x in enumerate(capacity,1):
            prefix[i] = prefix[i-1] + x
        ans = 0
        cnt = {}
        for r in range(2, n):
            l = r - 2
            cnt[(capacity[l], prefix[l+1])] = cnt.get((capacity[l], prefix[l+1]), 0) + 1
            ans += cnt.get((capacity[r], prefix[r] - capacity[r]), 0)
        return ans

        


        
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