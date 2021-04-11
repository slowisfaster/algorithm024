class Solution:
    def reverseWords(self, s: str) -> str:
        #return " ".join(s.split()[::-1])
        return " ".join(reversed(s.split()))

