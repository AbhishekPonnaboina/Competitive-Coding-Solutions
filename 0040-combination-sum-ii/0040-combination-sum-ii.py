class Solution:
    def combinationSum2(self, arr: List[int], k: int) -> List[List[int]]:
        arr.sort()
        res = []
        n = len(arr)
        sub =  []

        def generatesub(arr,sub,res,idx,suma):
            if suma == 0:
                res.append(sub.copy())
                return
            if suma < 0 or idx == n :
                return
            
            sub.append(arr[idx])
            generatesub(arr,sub,res,idx+1,suma-arr[idx])
            sub.pop()

            # same problem but we need to make slight changes like not inlcuding the same number while not including in the recursion thats what we need to change here thats it
            # we can also change this to binary search for the optimization 
            for j in range(idx+1,n):
                if arr[j] != arr[idx]:
                    generatesub(arr,sub,res,j,suma)
                    break
        
        generatesub(arr,sub,res,0,k)
        return res


        