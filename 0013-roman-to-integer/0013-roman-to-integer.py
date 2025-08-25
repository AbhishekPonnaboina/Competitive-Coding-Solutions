class Solution:
    def romanToInt(self, s: str) -> int:
        myhash = { 'I':1,"V":5 ,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        i = len(s) - 1

        while i >= 0:
            acc = myhash[s[i]]
            print("acc=",acc)
            j = i - 1
            while j >= 0 and myhash[s[i]] > myhash[s[j]]:
                print(myhash[s[i]],myhash[s[j]])
                acc -= myhash[s[j]]
                print("acc=",acc)
                j -= 1
            i = j
            res += acc
            print("res=",res)

        return res