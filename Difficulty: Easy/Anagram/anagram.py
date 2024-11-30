#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        if len(s1) != len(s2):
            return False
        count = [0]*256
        for i in range(len(s1)):
            count[ord(s1[i])] += 1
            count[ord(s2[i])] -= 1
        
        for i in count:
            if i != 0:
                return False
        return True
        
        
        
        
        
        
        
        
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends