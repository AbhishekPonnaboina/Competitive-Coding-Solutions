class Solution:
    def majorityElement(self, arr: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        n = len(arr)
        resarr =[]

        for i in range(n):
            hashmap[arr[i]] += 1

            if len(hashmap) <= 2:
                continue

            newhp = defaultdict(int)

            for k,v in hashmap.items():
                if v > 1:
                    newhp[k] = v - 1
            hashmap = newhp

        for k,v in hashmap.items():
            if arr.count(k) > n // 3:
                resarr.append(k)

        return resarr                      