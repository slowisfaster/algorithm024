class Solution:
    def firstUniqChar(self, s: str) -> int:
	 """
        freq = collections.Counter(s)
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i
        return -1
        """
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index)>0 else -1
        """
        return min([s.index(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])
        
