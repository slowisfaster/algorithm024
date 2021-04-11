class Solution:
    def myAtoi(self, s: str) -> int:
        ss = list(s.strip())
        if len(ss) == 0: return 0
        sign = -1 if ss[0] == '-' else 1
        if ss[0] in ['-', '+']: del ss[0]
        res, i = 0, 0
        while i < len(ss) and ss[i].isdigit():
            res = res*10 + ord(ss[i]) - ord('0')
            i += 1
        return max(-2**31, min(res*sign, 2**31-1))
