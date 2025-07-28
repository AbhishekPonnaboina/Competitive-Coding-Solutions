#User function Template for python3
class Solution:
	def setBits(self, n):
		# code here
		
		res = 0
		
		while n:
		    n = n & n - 1
		    res += 1
		return res