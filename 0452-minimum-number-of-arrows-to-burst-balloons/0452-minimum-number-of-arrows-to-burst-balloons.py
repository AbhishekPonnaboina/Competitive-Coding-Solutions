class Solution:
    def findMinArrowShots(self, arr: List[List[int]]) -> int:
        arr.sort()
        print(arr)
        #its just the similiar pattern of merging overlaps
        res = 0
        i = 0 
        lena = len(arr)
        while True:
            if i >= lena:
                break
            if res == 0:
                res += 1
                end = arr[i][1]
                i += 1
            else:
                for j in range(i,lena):
                    if  arr[j][0] <= end:
                        i += 1
                        print("im going in",arr[j])
                        end = min(end,arr[j][1])
                    else:
                        res += 1
                        i += 1
                        end =arr[j][1]
                        break


        return res
            
