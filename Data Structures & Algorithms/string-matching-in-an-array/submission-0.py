class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.trie = TrieNode()
    
    def insert(self, word):

        for i in range(len(word)):
            root = self.trie
            for w in word[i:]:
                if w not in root.childrens:
                    root.childrens[w] = TrieNode()
                root = root.childrens[w]
                root.count += 1
    
    def search(self, word):
        root = self.trie

        for w in word:
            if w not in root.childrens:
                return False
            root = root.childrens[w]
        
        return root.count > 1
    
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        trie = Trie()
        output = []

        for word in words:
            trie.insert(word)
        
        for word in words:
            if trie.search(word):
                output.append(word)
        
        return output

        