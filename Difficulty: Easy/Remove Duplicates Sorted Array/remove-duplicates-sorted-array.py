#User function template for Python

class Solution:
    def removeDuplicates(self, arr):
        #Code Here
        left = 1
        right = 1
        
        while right < len(arr):
            if arr[right] != arr[right-1]:
                arr[left] = arr[right]
                left += 1
            right += 1
        
        del arr[left:]
        #print(arr)
        return len(arr)
        
        
        
        
        
        
        
        
        
        return len(nums)

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    line = 1

    solution = Solution()

    for _ in range(t):
        if line < len(data):
            arr = list(map(int, data[line].split()))
            line += 1
            ans = solution.removeDuplicates(arr)
            for i in range(ans):
                print(arr[i], end=" ")
            print()
        print("~")

# } Driver Code Ends