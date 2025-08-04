class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        #mathematical approach 
        """y = x
        temp = 0
        while y != 0:
            lv = y % 10 
            temp = temp * 10 + lv
            y = y // 10
        if temp == x:
            return True
        return False
        """
        #str approach

        x = str(x)
        y=x[::-1]
        if x == y:
            return True 
        else:
            return False