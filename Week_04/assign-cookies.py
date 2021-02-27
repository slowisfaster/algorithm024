class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = 0
        for i in s:
            if n == len(g): break
            if i >= g[n]: n += 1
        return n
