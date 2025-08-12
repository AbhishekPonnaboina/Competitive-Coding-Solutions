from collections import defaultdict 
class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        hashmap = defaultdict(int)
        hashmap[0] = 1
        psum = 0
        count = 0

        for i in range(n):
            psum += arr[i]
            if (psum-k) in hashmap.keys():
                count += hashmap[psum-k]
            hashmap[psum] += 1


                
        return count 

        