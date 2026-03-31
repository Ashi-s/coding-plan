class Solution:
    def simplifyPath(self, path: str) -> str:
        # st = deque()
        # curr = ''
        # n = len(path)
        # i = 0
        # while i < len(path):
        #     curr = ''
        #     while i < len(path) and path[i] == '/':
        #         i += 1
            
        #     if i >= n:
        #         continue
            
        #     while i < len(path) and ('a' <= path[i] <= 'z' or 'A' <= path[i] <= 'Z' or path[i] == '_' or '0' <= path[i] <= '9'):
        #         curr += path[i]
        #         i += 1
            
        #     if i < len(path) and path[i] == '/':
        #         st.append(curr)
        #         continue
            
        #     while i < len(path) and path[i] == '.':
        #         curr += '.'
        #         i += 1
            
        #     if len(curr) == 1:
        #         pass
        #     elif len(curr) == 2:
        #         if st:
        #             st.pop()
        #     else:
        #         st.append(curr)

        # res = ''
        # while st:
            
        #     res += '/' + st.popleft()
        # return '/' if len(res) == 0 else res

        path = path.split("/")
        st = []

        for p in path:
            if p == "..":
                if st:
                    st.pop()
            elif  p != "" and p != ".":
                st.append(p)
            print(st)
        
        return "/" + "/".join(st)
            