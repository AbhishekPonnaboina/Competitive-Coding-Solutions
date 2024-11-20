
    
    
class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        resarr = []
        n = len(arr)
        if n == 0:
            return []
        
        res1, res2 = None, None
        count1, count2 = 0, 0
    
        # Step 1: Find potential majority elements
        for i in range(n):
            if res1 is not None and arr[res1] == arr[i]:
                count1 += 1
            elif res2 is not None and arr[res2] == arr[i]:
                count2 += 1
            elif count1 == 0:
                res1 = i
                count1 = 1
            elif count2 == 0:
                res2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
    
        # Step 2: Verify if the candidates appear more than n//3 times
        count1, count2 = 0, 0
        for i in range(n):
            if res1 is not None and arr[res1] == arr[i]:
                count1 += 1
            if res2 is not None and arr[res2] == arr[i]:
                count2 += 1
    
        if count1 > n // 3:
            resarr.append(arr[res1])
        if count2 > n // 3 and (res1 is None or arr[res1] != arr[res2]):
            resarr.append(arr[res2])
        resarr.sort()
    
        return resarr


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends