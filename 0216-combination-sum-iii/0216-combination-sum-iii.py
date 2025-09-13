class Solution:
    def combinationSum3(self, k: int, suma: int) -> List[List[int]]:
        ## you got this on your own mf progress ig
        ## niceee actually nice
        
        res = []
        sub = []

        def generatesub(suma,idx):
            if suma == 0 and len(sub) == k :          
                res.append(sub.copy())
                return
            if suma < 0 or len(sub) > k or idx == 9:
                return
            sub.append(idx+1)
            generatesub(suma-(idx+1),idx+1)
            sub.pop()
            generatesub(suma,idx+1)
        
        generatesub(suma,0)
        return res

