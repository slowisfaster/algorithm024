class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            k = d["".join(sorted(s))].append(s)
        return list(d.values())
