class Solution:
    def maxLength(self, arr):
        # code here
        # the basic approach would be of the genrating all the pairs like 
        # doing it in o(n**2) time like i to n - 1where i == currsum 
        #  +j but we got the prefix sum array
        
        n = len(arr)
        prefixarr = dict()
        maxi = 0
        suma = 0
        
        for i in range(n):
            suma += arr[i]
            if suma == 0:
                maxi = i + 1
            if suma not in prefixarr.keys():
                prefixarr[suma] = i
            else:
                maxi = max(maxi,i - prefixarr[suma])
        # print(prefixarr)
    
        return maxi
            