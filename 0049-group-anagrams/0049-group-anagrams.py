class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            split = "".join(sorted(list(s)))
            d[split].append(s)
        res = []
        for i, j in d.items():
            res.append(j)
        return res