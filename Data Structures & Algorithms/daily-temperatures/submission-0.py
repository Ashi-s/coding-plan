class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = [] #[index, value]
        output = [0] * len(temperatures)

        for idx, val in enumerate(temperatures):
            if not st:
                st.append([idx, val])
            elif val < st[-1][1]:
                st.append([idx, val])
            else:
                while st and val > st[-1][1]:
                    output[st[-1][0]] = idx - st[-1][0]
                    st.pop()
                st.append([idx, val])
        return output
            
        #simple
        # while st and val > st[-1][1]:
        #     output[st[-1][0]] = idx - st[-1][0]
        #     st.pop()
        # st.append([idx, val])

        