class Solution:
    def gcd(a,b):
        #Eucldiean algorithm
        """while a != b:
            if a>b:
                a=a-b
            if b>a:
                b=b-a
        return a"""
        if b == 0:
            return a
        else:
            gcd(a,b%a)

    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        return gcd(a,b)
        