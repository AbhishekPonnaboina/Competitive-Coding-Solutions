class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        pre = 1
        suf = 1
        res = -2 ** 31
        n = len(arr)

        for i in range(n):
            if pre == 0:
                pre= 1
            if suf == 0:
                suf = 1
            pre = pre * arr[i]
            suf = suf * arr[n-i-1]
            res = max(res,pre,suf)
        
        return res