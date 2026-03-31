class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if c in ['{', '(', '[']:
                st.append(c)
            elif c == '}' and st and st[-1] == '{':
                st.pop()
            elif c == ')' and st and st[-1] == '(':
                st.pop()
            elif c == ']' and st and st[-1] == '[':
                st.pop()
            else:
                return False
        
        return len(st) == 0
        