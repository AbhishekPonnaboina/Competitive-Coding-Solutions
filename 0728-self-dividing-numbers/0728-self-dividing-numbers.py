class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        resarr = []

        for i in range(left,right+1):
            res = len(str(i))
            dup = i

            while dup:
                div = dup % 10

                if div == 0 or i % div != 0:
                    break
                dup //= 10                
            else:
                resarr.append(i)
        return resarr