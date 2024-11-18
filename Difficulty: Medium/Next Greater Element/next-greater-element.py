# User function Template for python3

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        
        stack = []
        res = []*len(arr)
        
        for i in range(len(arr)-1,-1,-1):
            while (len(stack) > 0 and arr[i] >= stack[-1]):
                stack.pop()
            if len(stack)==0:
                res.append(-1)
            else:
                res.append(stack[-1])
            stack.append(arr[i])
        return res[::-1]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends