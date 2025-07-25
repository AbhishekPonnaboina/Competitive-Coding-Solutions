class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        mydict1 = {}
        mydict2 = {}
        
        for i in range(len(s1)):
            if s1[i] not in mydict1:
                mydict1[s1[i]] = s2[i]
            else:
                if mydict1[s1[i]] != s2[i]:
                    return False
            
            if s2[i] not in mydict2:
                mydict2[s2[i]] = s1[i]
            else:
                if mydict2[s2[i]] != s1[i]:
                    return False
        return True