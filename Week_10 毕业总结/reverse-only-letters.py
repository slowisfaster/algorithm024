class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        """
        c = [s for s in S if s.isalpha()]
        return ''.join([S[i] if not S[i].isalpha() else c.pop() for i in range(len(S))])
        """
        ans = []
        j = len(S) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(x)
        return "".join(ans)
                
