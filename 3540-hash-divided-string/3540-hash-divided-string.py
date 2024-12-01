class Solution:
    def stringHash(self, s: str, k: int) -> str:
        #myhash = dict()
        ord1 = 97
        """for i in range(26):
            myhash[chr(ord1)] = i
            ord1 += 1
        print(myhash)"""
        res1 = ""
        res = []
        for i in range(0,len(s),k):
            sub = s[i : i+k]
            res.append(sub)
        for i in res:
            sum1 = 0
            for ele in i:
                sum1 += ord(ele) - 97
            sum1 = sum1 % 26
            res1 += chr(97 + sum1) 

        return res1