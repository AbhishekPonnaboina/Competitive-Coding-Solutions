class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        
        count = 0

        for i in range(len(arr)):
            if arr[i]:
                arr[count],arr[i] = arr[i],arr[count]
                count += 1
        return arr
            
        