class Solution:
	def nthRowOfPascalTriangle(self, n):
	    # code here
	    if n == 0:
	        return []
	    if n == 1:
	        return [1]
	    res = [1]
	    
	    for i in range(1,n):
	        ans = res[-1]
	        ans = (ans*(n-i)) // i
	        res.append(ans)
	    return res