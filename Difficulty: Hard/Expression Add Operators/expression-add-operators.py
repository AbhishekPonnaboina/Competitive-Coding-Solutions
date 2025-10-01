class Solution:
    def findExpr(self, num, target):
        # code here
        ans = []
        n = len(num)

        def solve(idx,curr,prev,res):
            if idx == n:
                if res == target:
                    ans.append(curr)
                return
            sub = ''
            currres = 0
            for i in range(idx,n):
                if i > idx and num[idx] == '0':
                    break        
                sub += num[i]
                currres = currres * 10 + int(num[i])

                if idx == 0:
                    solve(i+1,sub,currres,currres)
                else:
                    solve(i+1,curr+'+'+sub,currres,res+currres)

                    solve(i+1,curr+'-'+sub,-currres,res-currres)
                    
                    solve(i+1,curr+'*'+sub,prev*currres,res - prev + (prev * currres))
            
        solve(0,'',0,0)
        return ans
        
        