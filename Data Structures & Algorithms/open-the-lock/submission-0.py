class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        visited = set(deadends)
        if "0000" in visited:
            return -1 
        q = deque([("0000", 0)]) # string value, count

        while q:
            val, count = q.popleft()

            if val == target:
                return count 

            for i in range(4):
                left = (int(val[i]) - 1 + 10) % 10
                right = (int(val[i]) + 1) % 10

                left_str = val[:i] + str(left) + val[i+1:]
                right_str = val[:i] + str(right) + val[i+1:]

                if left_str not in visited:
                    visited.add(left_str)
                    q.append((left_str, count+1))
                
                if right_str not in visited:
                    visited.add(right_str)
                    q.append((right_str, count+1))
        
        return -1
