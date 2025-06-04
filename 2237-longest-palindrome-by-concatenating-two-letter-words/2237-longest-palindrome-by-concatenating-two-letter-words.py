class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mydict = defaultdict(int)
        matched = defaultdict(int)
        res = 0

        for word in words:
            if word[0] == word[1]:
                if word in matched:
                    res += 4
                    del matched[word]
                else:
                    matched[word] += 1
    
            else:
                if word in mydict:
                    res += 4
                    mydict[word] -= 1
                    if mydict[word] == 0:
                        del mydict[word]
                else:
                    mydict[word[::-1]] += 1
        if matched:
            return res + 2
        return res
