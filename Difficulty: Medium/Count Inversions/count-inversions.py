class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        # Your Code Here
        def merge(l,mid,r):
            i=l
            j=mid+1
            temp=[]
            while i<=mid and j<=r:
                if arr[i]<=arr[j]:
                    temp.append(arr[i])
                    i+=1
                else:
                    temp.append(arr[j])
                    j+=1
                    inversions[0]+=mid-i+1
            if i<=mid: temp+=arr[i:mid+1]
            if j<=r: temp+=arr[j:r+1]
            for k in range(l,r+1):
                arr[k]=temp[k-l]
        
        def mergeSort(l,r):
            if l>=r:
                return
            mid=(l+r)//2
            mergeSort(l,mid)
            mergeSort(mid+1,r)
            merge(l,mid,r)
        
        inversions=[0]
        n=len(arr)
        mergeSort(0,n-1)
        return inversions[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends