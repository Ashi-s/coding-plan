class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        i = 0

        while i < len(asteroids):

            if asteroids[i] > 0:
                st.append(asteroids[i])
            elif not st or st[-1] < 0:
                st.append(asteroids[i])
            else:
                flag = True
                while st and st[-1] > 0:
                    if st[-1] == abs(asteroids[i]):
                        st.pop()
                        flag = False
                        break
                    elif st[-1] > abs(asteroids[i]):
                        flag = False
                        break
                    else:
                        st.pop()
                        flag = True

                if flag:
                    st.append(asteroids[i])
            
            i += 1
        
        return st