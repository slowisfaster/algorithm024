class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #return s[:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k) if s else ""
	s=[s[i:i+k] for i in range(0, len(s), k)]
        for i in range(0, len(s), 2):
            s[i] = s[i][::-1]
        return "".join(s)		
