class Solution:
    def reverseWords(self, s: str) -> str:
        #return ' '.join([x[::-1] for x in s.split()])
        #return ' '.join(s.split()[::-1])[::-1]
        return ' '.join(map(lambda x:x[::-1], s.split()))
