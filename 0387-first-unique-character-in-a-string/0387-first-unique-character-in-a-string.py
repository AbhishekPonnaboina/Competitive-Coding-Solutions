class Solution:
    def firstUniqChar(self, s: str) -> int:
        myhash = Counter(s)
        
        for i in range(len(s)):
            if myhash[s[i]] == 1:
                return i
        return -1