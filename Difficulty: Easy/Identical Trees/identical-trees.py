'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,r1, r2):
        # Code here
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        if r1.data != r2.data:
            return False
        return self.isIdentical(r1.left,r2.left) and self.isIdentical(r1.right,r2.right)