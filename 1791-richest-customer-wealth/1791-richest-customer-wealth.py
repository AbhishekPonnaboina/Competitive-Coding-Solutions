class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0

        for i in range(len(accounts)):
            suma = 0

            for j in range(len(accounts[0])):
                suma += accounts[i][j]
            
            if suma > maxi:
                maxi = suma
        
        return maxi