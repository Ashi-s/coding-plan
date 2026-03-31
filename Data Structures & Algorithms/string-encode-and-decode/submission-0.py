class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        output = []
        i, j = 0, 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = j + length
            output.append(s[i:j+1])

            i = j+1

        return output
