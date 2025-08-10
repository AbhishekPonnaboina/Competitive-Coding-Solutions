class Solution:
    def sortPermutation(self, arr: List[int]) -> int:
        n = len(arr)
        k = -1
        ar = True

        for i in range(n):
            if arr[i] != i:
                ar = False
                k = k & arr[i]
                k = k & i
        
        return 0 if ar else k