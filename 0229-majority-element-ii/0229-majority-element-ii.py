class Solution:
    def majorityElement(self, arr: List[int]) -> List[int]:

        ele1 = float("-inf")
        ele2 = float("-inf")
        cnt1 = 0
        cnt2 = 0

        res = []*2

        for i in range(len(arr)):
            if cnt1 == 0 and arr[i] != ele2:
                cnt1 += 1
                ele1 = arr[i]
            elif cnt2 == 0 and arr[i] != ele1:
                cnt2 += 1
                ele2 = arr[i]
            elif arr[i] == ele1:
                cnt1 += 1
            elif arr[i] == ele2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1 = 0
        cnt2 = 0

        for i in range(len(arr)):
            if arr[i] == ele1:
                cnt1 += 1
            if arr[i] == ele2:
                cnt2 += 1

        if cnt1 > len(arr) // 3:
            res.append(ele1)
        if cnt2 > len(arr) // 3:
            res.append(ele2) 
        
        return res










        """
        second better approach here 
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
        """      