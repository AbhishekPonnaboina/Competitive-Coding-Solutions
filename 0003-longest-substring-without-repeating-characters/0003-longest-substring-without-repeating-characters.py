class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxlen = 0

        for i in range(n):
            myhash = defaultdict(int)
            for j in range(i,n):
                if myhash[s[j]] == 1:
                    break
                lena = j - i + 1
                maxlen = max(lena,maxlen)
                myhash[s[j]] = 1
        return maxlen

        