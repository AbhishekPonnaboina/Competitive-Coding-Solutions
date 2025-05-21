#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
		# code here
		myhash = {}
		
		for i,val in enumerate(arr):
		    if target - val in myhash:
		        return True
		    myhash[val] = i
	    return False