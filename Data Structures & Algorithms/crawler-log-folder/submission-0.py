class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = 0

        for l in logs:
            if l == './':
                continue
            elif l == '../':
                if steps != 0:
                    steps -= 1
            else:
                steps += 1
        
        return steps