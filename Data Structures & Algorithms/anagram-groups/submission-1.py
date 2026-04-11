class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            sort_s = "".join(sorted(s))
            d[sort_s].append(s)

        return list(d.values())