class Trie:
    def __init__(self):
        self.childrens = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = Trie()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.childrens:
                curr.childrens[w] = Trie()
            
            curr = curr.childrens[w]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.childrens:
                return False
            curr = curr.childrens[w]
        return curr.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for p in prefix:
            if p not in curr.childrens:
                return False
            curr = curr.childrens[p]
        
        return True
        
        