class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
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



        # you could not able to figure out the multiplication operator formula
        # res = 0
        # n = len(num)
        # resarr = []
        # sub = ''
        # opera = []

        # def recur(i,sub,res):
        #     print("sub=",sub)
        #     print("i",i)
        #     print("res",res)
        #     print("------------------------------------")
        #     if target == res:
        #         resarr.append(sub[:-1])
        #         return
        #     if i == n:
        #         return

        #     opera.append('+')
        #     recur(i+1,sub+num[i]+'+',res+int(num[i]))
        #     opera.pop()

        #     opera.append('-')
        #     recur(i+1,sub+num[i]+'-',res-int(num[i]))
        #     opera.pop()

        #     if opera and opera[-1] == '-':
        #         a = res - int(num[i])
        #         b = res - a
        #         recur(i+1,sub+num[i]+'*',(b*int(num[i]) + a))
            
        #     elif opera and opera[-1] == '+':
        #         a = res + int(num[i])
        #         b = res + a
        #         recur(i+1,sub+num[i]+'*',(b*int(num[i]) - a))
        #     else:
        #         opera.append('*')
        #         recur(i+1,sub+num[i]+'*',res*int(num[i]))
        #         opera.pop()
            
            

        # recur(0,sub,0)    
        # return resarr