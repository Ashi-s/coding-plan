class Trie:
    def __init__(self):
        self.childrens = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w not in curr.childrens:
                curr.childrens[w] = Trie()
            curr = curr.childrens[w]
        
        curr.isWord = True
        

    def search(self, word: str) -> bool:

        def helper(idx, root):
            curr = root
            if idx >= len(word):
                return curr.isWord
            
            if word[idx] in curr.childrens:
                curr = curr.childrens[word[idx]]
                return helper(idx+1, curr)
            elif word[idx] == ".":
                for c in curr.childrens.values():
                    if helper(idx+1, c):
                        return True
                return False
            else:
                return False
        
        return helper(0, self.root)
                    
            
