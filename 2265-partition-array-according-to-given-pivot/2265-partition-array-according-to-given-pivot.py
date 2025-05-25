class Solution:
    def pivotArray(self, arr: List[int], pivot: int) -> List[int]:
        n = len(arr)
        nums = [0]*len(arr)
        i1,j1 = 0,len(arr) - 1
        i2,j2 = 0,len(arr) - 1

        while i1 < n and j1 >= 0:
            if arr[i1] < pivot:
                nums[i2] = arr[i1]
                i2 += 1
            if arr[j1] > pivot:
                nums[j2] = arr[j1]
                j2 -= 1
            i1 += 1
            j1 -= 1
        for i in range(i2,j2+1):
            nums[i] = pivot

        return nums


