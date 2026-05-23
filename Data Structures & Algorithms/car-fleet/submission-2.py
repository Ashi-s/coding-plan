class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(p, s) for p, s in zip(position, speed)]

        arr.sort(reverse=True)
        st = []

        for p, s in arr:
            t = (target - p) / s

            if st and st[-1] >= t:
                continue
            
            st.append(t)
        
        return len(st)
