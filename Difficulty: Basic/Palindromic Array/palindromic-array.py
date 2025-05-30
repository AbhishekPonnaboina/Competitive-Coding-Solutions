# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    # Code here
    for i in arr:
        dup = i
        rev = 0
        while dup:
            rem = dup % 10
            rev = rev* 10 + rem
            dup //= 10
        if i != rev:
            return False
    return True