class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.count = 0

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = TrieNode()
        

        for word in words:
            curr = trie
            for w in word:
                if w not in curr.childrens:
                    curr.childrens[w] = TrieNode()
                curr = curr.childrens[w]
                curr.count += 1
                
        curr = trie
        for p in pref:
            if p not in curr.childrens:
                return 0
            curr = curr.childrens[p]
        
        return curr.count
        

        
