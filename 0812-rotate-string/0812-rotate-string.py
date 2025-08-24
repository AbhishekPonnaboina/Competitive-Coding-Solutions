class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        a = len(s)
        b = len(goal)

        if a != b:
            return False 
        
        for i in range(a):
            cpy = s[i+1:] + s[:i+1]
            if cpy == goal:
                return True
        else:
            return False