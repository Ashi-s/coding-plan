class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.isEnd = True
        

    def search(self, word: str) -> bool:
        
        def helper(idx, root):
            curr = root

            if idx >= len(word):
                return curr.isEnd
            
            if word[idx] in curr.children:
                curr = curr.children[word[idx]]
                return helper(idx+1, curr)
            elif word[idx] == ".":
                for c in curr.children.values():
                    if helper(idx+1, c):
                        return True
                return False
            else:
                return False
        
        return helper(0, self.root)

            
