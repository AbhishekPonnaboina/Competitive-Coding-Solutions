class Solution:
    def printTillN(self,N,i=1):
    	#code here 
    	if i > N:
    	    return
        print(i,end=" ")
        i += 1
        self.printTillN(N,i)