
class Solution:
    def checkIfPangram(self, s : str) -> bool:
        myhash = set()

        for i in s:
            myhash.add(i)
        
        return len(myhash) == 26
        