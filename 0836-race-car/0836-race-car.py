
from collections import deque
class Solution:
    def racecar(self, target: int) -> int:

        myque = collections.deque([(0,0,1)])
        visited = set()

        while myque:
            m , p , s = myque.popleft()
            if p == target:
                return m

            if (p,s) in visited:
                continue
            else:
                visited.add((p,s))
                myque.append((m+1,p+s,s*2))
                if (p+s > target and s > 0) or ((p+s < target and s < 0)):
                    if s > 0:
                        s = -1
                    else:
                        s = 1
                    myque.append((m+1,p,s))  