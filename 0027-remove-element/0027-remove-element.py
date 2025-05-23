class Solution:
    def removeElement(self, arr: List[int], val: int) -> int:
        i = 0
        j = len(arr) - 1

        while i <= j :
            while i <= j and arr[i] != val :
                i += 1
            while i <= j and arr[j] == val:
                j -= 1
            if i < j:
                arr[i],arr[j] = arr[j],arr[i]

        return j + 1


