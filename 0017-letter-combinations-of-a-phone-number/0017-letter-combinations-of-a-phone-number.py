class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #when using strings immutable data type dont try to backtrack manually
        #we just need not do that python creates a new object
        #lesson learned on trying to change an immutable data type 
        #pass by reference-to-immutable-object. that means creating an 
        # new string and passing the value to in the recdursion call itself
        #so we no need to change that particular backtracking

        if not digits:
            return []
        n = len(digits)
        
        dial = [[],[], ['a', 'b', 'c'],       
                    ['d', 'e', 'f'],        
                    ['g', 'h', 'i'],        
                    ['j', 'k', 'l'],        
                    ['m', 'n', 'o'],        
                    ['p', 'q', 'r', 's'],   
                    ['t', 'u', 'v'],        
                    ['w', 'x', 'y', 'z'],   
                ]
        sub = ""
        res = []

        def generatesub(idx,sub):

            if len(sub) == n:
                res.append(sub)
                return
            if idx >= n:
                return
            sublist = int(digits[idx]) #2
            for i in range(len(dial[sublist])):
                generatesub(idx+1,sub+dial[sublist][i])

        generatesub(0,sub) ## 2
        return res
