class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #it has 3 different questions and you check all its kinda important you could say
        if numRows == 0:
            return []
        res =[]

        for i in range(1,numRows+1):
            #here i is nothing but the row number and n in the formula of n c r
            temp = [1]
            ans = 1
            for j in range(1,i):
                # here j is nothing but the col number and r  in the formula of n c r 
                ans = (ans * (i - j)) // j
                temp.append(ans)
            res.append(temp)
        return res