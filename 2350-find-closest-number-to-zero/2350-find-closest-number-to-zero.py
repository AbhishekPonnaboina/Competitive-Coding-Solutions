class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        res = []
        mini = 10**6
        ans = 0

        for i in nums:
            if i == 0:
                return 0
            j = abs(i)

            if mini == j:
                res.append(i)
                continue
            else:
                if mini > j:
                    mini = j
                    ans = i
        
        if not res:                           
            return ans
        res.append(ans)
        return max(res)