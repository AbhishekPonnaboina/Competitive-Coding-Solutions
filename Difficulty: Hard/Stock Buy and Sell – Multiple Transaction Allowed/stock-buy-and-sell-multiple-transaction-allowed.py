from typing import List


class Solution:
    def maximumProfit(self, a) -> int:
        # code here
        b, c = 0, len(a)
        d = 0
        for e in range(1, c):
            f = a[e] - a[e - 1]
            if f > 0:
                d += f
        return d


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)

# } Driver Code Ends