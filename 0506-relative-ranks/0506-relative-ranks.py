class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        s=sorted(score,reverse=True)
        # print(s)

        myhash = dict()

        for i in range(n):
            if i == 0:
                myhash[s[i]] = "Gold Medal"
                continue
            if i == 1:
                myhash[s[i]] = "Silver Medal"
                continue
            if i == 2:
                myhash[s[i]] = "Bronze Medal"
                continue
            myhash[s[i]] = str(i + 1)
            
        for i in range(n):
            score[i] = myhash[score[i]]
            
        
        # print(myhash)
        return score        
        
        