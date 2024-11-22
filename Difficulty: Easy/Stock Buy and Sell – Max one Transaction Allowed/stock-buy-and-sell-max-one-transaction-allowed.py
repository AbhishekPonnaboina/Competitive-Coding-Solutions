class Solution:
    def maximumProfit(self, prices):
        # code here
        a = float('inf')
        b = 0
        for c in prices:
            a = min(a, c)
            b = max(b, c - a)
        return b
        
        
        
        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends