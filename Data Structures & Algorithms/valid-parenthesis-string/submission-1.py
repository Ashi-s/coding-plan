class Solution:
    def checkValidString(self, s: str) -> bool:
        st1 = []
        st2 = []

        for i in range(len(s)):
            if s[i] == '(':
                st1.append(i)
            elif s[i] == '*':
                st2.append(i)
            else:
                if st1:
                    st1.pop()
                elif st2:
                    st2.pop()
                else:
                    return False
            # print(st1, st2)
        
        while st1 and st2:
            if st1.pop() > st2.pop():
                return False
        
        return not st1
        
        
        