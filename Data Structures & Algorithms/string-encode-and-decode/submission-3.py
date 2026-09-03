class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i

            # Find the '#' after the length
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            # Read exactly `length` characters
            start = j + 1
            end = start + length

            ans.append(s[start:end])

            i = end

        return ans
