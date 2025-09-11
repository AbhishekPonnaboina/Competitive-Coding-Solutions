class Solution:
    def combinationSum(self, candidates: List[int], k: int) -> List[List[int]]:
        ans = []
        sub = []
        def generatesub(idx,sub,suma):
            if suma == 0:
                ans.append(sub.copy())
                # like adding it to our list the answer and returning it
                return 
            if idx == len(candidates) or suma < 0: #base caseee
                return
            sub.append(candidates[idx])
            generatesub(idx,sub,suma - candidates[idx])
            sub.pop()
            generatesub(idx+1,sub,suma)
        
        generatesub(0,sub,k)
        
        return ans




