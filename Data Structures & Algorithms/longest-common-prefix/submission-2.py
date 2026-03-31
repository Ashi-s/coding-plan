class TrieNode:
    def __init__(self):
        self.neighbors ={}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in curr.neighbors:
                curr.neighbors[w] = TrieNode()
            curr = curr.neighbors[w]
    
    def lcp(self):
        curr = self.root.neighbors
        count = 0

        while True:
            if len(curr.keys()) == 1:
                count += 1
                curr = list(curr.values())[0].neighbors
            else:
                break
        return count
            

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = Trie()
        smallest = float('inf')

        for s in strs:
            if not s:
                return ""
            root.insert(s)
            smallest = min(smallest, len(s))

        
        res = root.lcp()
        res = min(smallest, res)
        
        if res == 0:
            return ""
        else:
            return strs[0][:res]
        
        
        