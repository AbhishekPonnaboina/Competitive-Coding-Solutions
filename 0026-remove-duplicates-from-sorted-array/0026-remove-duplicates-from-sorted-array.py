class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        left = 1
        right = 1

        while right < len(arr):

            if arr[right] != arr[right-1]:
                arr[left] = arr[right]
                left += 1
            right += 1
        
        print(arr)
        return left
        












        #your way
        """fir = nums[0]
        count = 1

        for i in range(1,len(nums)):
            if nums[i] == fir:              
                continue
            fir = nums[i]
            nums[i],nums[count] = nums[count],nums[i]
            count += 1

        del nums[count:]
        return len(nums)"""