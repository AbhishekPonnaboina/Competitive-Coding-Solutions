class Solution:
	def subsetSums(self, arr):
		# code here
		
		ans = []
		n = len(arr)
        def generatesubset(arr,suma,idx):
            
		    if idx == n:
		        ans.append(suma)
		        return
	        generatesubset(arr,suma+arr[idx],idx+1)
		    generatesubset(arr,suma,idx+1)
	    generatesubset(arr,0,0)
		return ans
		