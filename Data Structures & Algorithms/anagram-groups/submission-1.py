class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            sort = ''.join(sorted(s))
            if sort not in d:
                d[sort] = [s]
            else:
                d[sort].append(s)
        
        return list(d.values())