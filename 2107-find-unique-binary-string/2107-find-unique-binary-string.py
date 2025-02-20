class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        q = collections.deque()
        q.append('0')
        q.append('1')

        n = len(nums)
        res = []

        while q:
            sub = q.popleft()
            if len(sub) == n:
                res.append(sub)
                continue
            
            First = sub + '0'
            Second = sub + '1'
            q.append(First)
            q.append(Second)
        
        for i in res :
            if i not in nums:
                return i

