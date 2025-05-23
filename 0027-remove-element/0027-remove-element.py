class Solution:
    def removeElement(self, arr: List[int], val: int) -> int:
        i = 0
        j = len(arr) - 1

        while i <= j :
            while i < len(arr) and arr[i] != val :
                i += 1
            while 0 <= j and arr[j] == val:
                j -= 1
            if i < j:
                arr[i],arr[j] = arr[j],arr[i]

        return j + 1


