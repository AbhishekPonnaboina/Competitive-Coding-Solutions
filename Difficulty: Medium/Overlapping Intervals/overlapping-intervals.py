class Solution:
	def mergeOverlap(self, arr):
		# Code here
		
		arr.sort()
		res = []
		
		for i in range(len(arr)):
		    if len(res) == 0:
		        res.append(arr[i])
		    if arr[i][0] > res[-1][1]:
		        res.append(arr[i])
		    else:
		        maxi = max(arr[i][1],res[-1][1])
		        res[-1][1] = maxi
	    return res