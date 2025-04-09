class Node:
    def __init__(self):
        self.children = {}
        self.word_end = False
class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        current_node = self.root
        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch] = Node()
            current_node = current_node.children[ch]
        current_node.word_end = True
        return 
    
        

    def search(self, word: str) -> bool:
        current_node  = self.root
        for ch in word:
            if ch not in current_node.children:
                return False
            current_node = current_node.children[ch]
        return current_node.word_end        

    def startsWith(self, word: str) -> bool:
        current_node = self.root
        for ch in word:
            if ch not in  current_node.children:
                return False
            current_node = current_node.children[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)