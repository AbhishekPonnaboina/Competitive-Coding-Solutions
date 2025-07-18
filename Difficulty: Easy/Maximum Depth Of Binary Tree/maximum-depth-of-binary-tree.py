#User function Template for python3


class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:

    def maxDepth(self, root):
        
        def maxde(root):
            if not root:
                return 0
            return max(maxde(root.left),maxde(root.right)) + 1
        
        return maxde(root)
