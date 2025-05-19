class Solution:
    def check(self, arr: List[int]) -> bool:

        #optimal way and tbh sexy way
        n = len(arr)
        count = 1

        for i in range(1,2*n):
            if arr[(i-1)%n] <= arr[i%n]:
                count += 1
            else:
                count = 1

            if count == n:
                return True
        return n == 1






        #brute force
        """for i in range(len(arr)):
            res = arr.pop(0)
            arr.append(res)

            if arr == sorted(arr):
                return True
        return False"""