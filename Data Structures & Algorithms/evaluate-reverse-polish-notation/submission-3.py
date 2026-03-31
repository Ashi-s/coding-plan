class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for t in tokens:
            print(st)
            if t in ['+', '-', '*', '/']:
                a = st.pop()
                b = st.pop()
                if t == '+':
                    st.append(b+a)
                if t == '-':
                    st.append(b-a)
                if t == '*':
                    st.append(a*b)
                if t == '/':
                    st.append(int(float(b/a)))
            else:
                st.append(int(t))
        return st[-1]
        