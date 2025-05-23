class Solution:
    def sortArrayByParityII(self, arr: List[int]) -> List[int]:
        

        i = 0
        j = len(arr) - 1

        while i < len(arr) and j >= 0:
            while i < len(arr) and arr[i] % 2 == 0  :
                i += 2
            while  j >= 0  and arr[j] % 2 == 1 :
                j -= 2 
            if i < len(arr) and j >= 0:            
                arr[i],arr[j] = arr[j],arr[i]
        return arr
              