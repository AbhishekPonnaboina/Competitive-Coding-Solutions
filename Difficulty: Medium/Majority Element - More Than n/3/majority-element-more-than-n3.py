class Solution:
    def findMajority(self, arr):
        # code here
        n = len(arr)
        if n < 1:
            return []
        
        res = []*2
        
        ele1 = float("-inf")
        ele2 = float("-inf")
        cnt1,cnt2 = 0,0
        
        for i in range(n):
            if cnt1 == 0 and ele2 != arr[i]:
                cnt1 += 1
                ele1 = arr[i]
            elif cnt2 == 0 and ele1 != arr[i]:
                cnt2 += 1
                ele2 = arr[i]
            elif ele1 == arr[i]:
                cnt1 += 1
            elif ele2 == arr[i]:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1,cnt2 = 0,0
        
        for i in range(n):
            if arr[i] == ele1:
                cnt1+=1
            if arr[i] == ele2:
                cnt2 +=1
        
        if cnt1 > n // 3:
            res.append(ele1)
        if cnt2> n // 3:
            res.append(ele2)
        
        return sorted(res)