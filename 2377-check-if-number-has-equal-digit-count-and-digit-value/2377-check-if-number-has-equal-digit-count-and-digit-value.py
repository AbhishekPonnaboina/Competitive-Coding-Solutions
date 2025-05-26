from collections import Counter
class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        for i in range(len(num)):
            #print(num[i],c[str(i)])
            if int(num[i]) != c[str(i)]:
                break
        else:
            return True
        return False