class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #optimal approach like - here count so pointers 

        res = 0
        n = len(s)
        hashmap = dict()

        for r in range(n):
            hashmap[s[r]] = r
            if len(hashmap) == 3:
                print(hashmap)
                mini = min(hashmap.values())
                res += mini + 1
        return res
            








        #naive approach yeah like expected Tle

        # res = 0
        # n = len(s)

        # for i in range(n):
        #     arr = [0] * 3
        #     for j in range(i,n):
        #         arr[ord(s[j]) - ord('a')] = 1

        #         if sum(arr) == 3:
        #             res += 1
        #             break
        # return res
        















        # n = len(s)
        # left = 0
        # cnt = 0
        # d = collections.defaultdict(int)
        # for right in range(n):
        #     d[s[right]] += 1
        #     while len(d.keys()) == 3:
        #         cnt += n - right
        #         d[s[left]] -= 1
        #         if d[s[left]] == 0:
        #             d.pop(s[left])
        #         left += 1
        # return cnt
                
