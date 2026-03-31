class Solution:
    def partition(self, s: str) -> List[List[str]]:


        def helper(i):
            if i >= len(s):
                res.append(curr.copy())
            
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    curr.append(s[i:j+1])
                    helper(j+1)
                    curr.pop()
        
        res = []
        curr = []
        helper(0)
        return res