class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjency = {}
        tickets.sort()

        for from_i, to_i in tickets[::-1]:
            if from_i not in adjency:
                adjency[from_i] = [to_i]
            else:
                adjency[from_i].append(to_i)
        
        st = ['JFK']
        res = []
        
        while st:
            curr = st[-1]
            if not adjency.get(curr, []):
                res.append(st.pop())
            else:
                st.append(adjency[curr].pop())
        
        return res[::-1]


