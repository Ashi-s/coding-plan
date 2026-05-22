class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                st.append(int(t))
            else:
                a, b = st.pop(), st.pop()
                if t == '+':
                    st.append(a+b)
                elif t == '-':
                    st.append(b-a)
                elif t == '*':
                    st.append(a*b)
                elif t == '/':
                    st.append(int(float(b/a)))
            
        return st[-1]