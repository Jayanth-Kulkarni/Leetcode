class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for i in strs:
            map["".join(sorted(i))].append(i)
        res = []
        for key,value in map.items():
            res.append(value)
        return res