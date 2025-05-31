#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        # your code here
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        series = [0, 1]
        for i in range(2, n):
            next_number = series[-1] + series[-2]
            series.append(next_number)
        return series