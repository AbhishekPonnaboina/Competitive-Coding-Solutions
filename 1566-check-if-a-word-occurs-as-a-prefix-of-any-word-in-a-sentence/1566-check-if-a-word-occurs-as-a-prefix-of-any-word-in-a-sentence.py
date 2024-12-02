class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        mylist = sentence.split(" ")
        for i in range(len(mylist)):
            if mylist[i][:len(searchWord)] == searchWord:
                return i + 1
        return -1