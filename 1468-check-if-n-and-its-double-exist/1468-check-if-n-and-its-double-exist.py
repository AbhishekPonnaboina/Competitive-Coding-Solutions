class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        myhash = set()

        for i in arr:
            if (2*i in myhash) or (i/2 in myhash):
                return True
            myhash.add(i)


        return False
        