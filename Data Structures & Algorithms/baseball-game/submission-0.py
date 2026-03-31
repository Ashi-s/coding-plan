class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        i = 0

        while i < len(operations):
            if operations[i] == '+':
                st.append(int(st[-1]) + int(st[-2]))
            elif operations[i] == 'D':
                st.append(int(st[-1]) * 2)
            elif operations[i] == 'C':
                st.pop()
            else:
                st.append(operations[i])
            i += 1

        return sum([int(i) for i in st])
        