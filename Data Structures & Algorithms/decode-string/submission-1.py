class Solution:
    def decodeString(self, s: str) -> str:
        st = []

        for i in s:
            if i != ']':
                st.append(i)
            else:
                tmp = []
                curr = ''
                while st[-1] != '[':
                    tmp.append(st.pop())
                for i in range(len(tmp)-1, -1, -1): #get chars and reverse
                    curr += tmp[i]
                
                if st and st[-1] == '[': 
                    st.pop()
                
                nums = []
                while st and st[-1].isdigit():
                    nums.append(st.pop())
                
                k = 0
                for i in range(len(nums)-1, -1, -1): # get nums in reverse 
                    k = (k * 10) + int(nums[i])
                
                st.append(k * curr)
                print(f"k-{k}, st-{st}, curr - {curr}")
        
        return ''.join(st)

                
