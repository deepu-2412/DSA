class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ls = [-1,-1,-1]
        c = 0
        for i in range(0,len(s)):
            ls[ord(s[i]) - ord('a')] = i
            if -1 not in ls:
                c = c + (1 + min(ls))
        return c
