#User function Template for python3

class Solution:
	def singleNum(self, arr):
		# Code here
		xor = 0
		for i in arr:
		    xor ^= i
	    bit =  ( xor - 1 & xor ) ^ xor
	    
	    setbit = 0
	    notsetbit = 0
	    
	    for i in arr:
	        if i & bit:
                setbit ^= i
            else:
                notsetbit ^= i
        
        if setbit > notsetbit:
            return [notsetbit,setbit]
        return [setbit,notsetbit]