class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        for i in range(len(s)):
            res = s[i:] + s[:i]
            if res == goal:
                return True
        return False