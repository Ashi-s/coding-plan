class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [[p,s] for p,s in zip(position, speed)]

        st = []

        for p, s in sorted(arr)[::-1]:
            # dis = sp * t
            time = (target - p) / s

            if st and time <= st[-1]:
                continue

            st.append(time)

        return len(st)     