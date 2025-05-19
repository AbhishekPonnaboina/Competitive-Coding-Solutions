class Solution:
    def check(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            res = arr.pop(0)
            arr.append(res)

            if arr == sorted(arr):
                return True
        return False