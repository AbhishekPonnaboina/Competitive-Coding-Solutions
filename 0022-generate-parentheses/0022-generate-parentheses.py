class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def generate(mystr,Open,Close,n):
            if len(mystr) == 2*n:
                res.append(mystr)
                return
            if Open < n:
                generate(mystr+"(",Open+1,Close,n)
            if Close < Open:
                generate(mystr+")",Open,Close+1,n)
            
        generate("",0,0,n)
        return res
            # ["(()()())",
            # "((()()))",
            # "((())())",
            # "()()(())",
            # "(()())()",
            # "(()(()))"
            # ,"(())()()",
            # "()(()())",
            # "()(())()",
            # "()((()))",
            # "((()))()",
            # "()()()()",
            # "(((())))"]