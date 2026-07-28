class Solution:

    def encode(self, strs: List[str]) -> str:
        concatstr = ''
        concatstr = ''.join(str(len(i)) + '#' + i for i in strs)
        return concatstr

    def decode(self, s: str) -> List[str]:
        returnlist = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            content = s[j + 1 : j+ 1 + length]
            returnlist.append(content)
            i = j + 1 + length
        return returnlist
