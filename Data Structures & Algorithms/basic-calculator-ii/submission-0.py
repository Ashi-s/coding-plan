class Solution:
    def calculate(self, s: str) -> int:
        st = []
        op = '+'
        num = 0
        s = s.replace(' ', '')

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            
            if (not s[i].isdigit()) or i == len(s)-1:
                if op == '+':
                    st.append(num)
                elif op == '-':
                    st.append(-num)
                elif op == '*':
                    val = st.pop()
                    st.append(val * num)
                else:
                    val = st.pop()
                    st.append(int(val / num))
                
                op = s[i]
                num = 0
        
        return sum(st)

