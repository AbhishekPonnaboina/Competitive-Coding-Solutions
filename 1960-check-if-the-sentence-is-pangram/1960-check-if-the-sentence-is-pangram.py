
class Solution:
    def checkIfPangram(self, s : str) -> bool:
        myhash = dict()

        for i in range(26):
            myhash[chr(i+97)] = 1
        
        for i in s:
            myhash[i] = 0
        
        for k,v in myhash.items():
            if v == 1:
                return False
        return True
        