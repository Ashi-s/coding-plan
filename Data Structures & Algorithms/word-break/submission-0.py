class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root

        for w in word:
            if w not in node.childrens:
                node.childrens[w] = TrieNode()
            node = node.childrens[w]
        
        node.isWord = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        # We need a memo to keep track of indices we've already checked
        # otherwise, LeetCode will give you a "Time Limit Exceeded"
        memo = {}

        def helper(start_idx):
            # If we reached the end, we successfully broke the string!
            if start_idx == len(s):
                return True
            
            if start_idx in memo:
                return memo[start_idx]

            curr = trie.root  # Always start at the Trie root for a new word
            
            # This loop implements your "loop over string s" logic
            for i in range(start_idx, len(s)):
                char = s[i]
                
                if char not in curr.childrens:
                    # No word in the dictionary starts with this prefix, stop searching this path
                    break
                
                curr = curr.childrens[char]
                
                # "When I see a word in trie that has isWord true..."
                if curr.isWord:
                    # "...then I start a new helper"
                    if helper(i + 1):
                        memo[start_idx] = True
                        return True
            
            memo[start_idx] = False
            return False

        return helper(0)
        