class Solution:
    def reversePairs(self, arr: List[int]) -> int: 

        def mergesort(low,high):
            if low >= high:
                return 0
            mid = (low+ high) // 2
            count = mergesort(low,mid) + mergesort(mid+1,high)
           
            i = low
            j = mid + 1
            while i <= mid and j <= high:
                # print("arr left=",arr[i])
                # print("arr right=",arr[j]) 
                
                if arr[i] > 2 * arr[j]:
                    count += mid - i + 1
                    j += 1
                else:
                    i += 1 

            temp = []
            left = low
            right = mid + 1 
                   
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1

            while left <= mid:
                temp.append(arr[left])
                left += 1
            while right <= high:
                temp.append(arr[right])
                right += 1
            
            
            
            for i in range(len(temp)):
                arr[low + i] = temp[i]
            return count

        count = 0
        n = len(arr) - 1
        return mergesort(0,n)
        