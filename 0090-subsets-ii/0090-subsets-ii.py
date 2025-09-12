class Solution:
    def subsetsWithDup(self, arr: List[int]) -> List[List[int]]:
        #one way is to generate all the lists and then use a set to keep only the 
        #the unique once but we need extra time complexity for converting into set 
        # and then again back to list<list>

        #now we have the other solution where in recursion itself we can avoid the duplicates
        #and that approach is nice and we use the sorting


        arr.sort()
        sub = []
        res = []
        n = len(arr) 

        def generateSubSets(arr,res,sub,idx,n):
            # print(sub.copy())
            # print("-------------------------------------")
            res.append(sub.copy())
            for i in range(idx,n):
                if i > idx and arr[i] == arr[i-1]:
                    continue
                sub.append(arr[i])
                generateSubSets(arr,res,sub,i+1,n)
                sub.pop()
        generateSubSets(arr,res,sub,0,n)
        return res


