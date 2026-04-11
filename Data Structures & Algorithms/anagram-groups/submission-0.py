class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            for t in d.keys():
                if self.isAnagram(s, t):
                    d[t].append(s)
                    
            sort_s = "".join(sorted(s))
            if sort_s not in d.keys():
                d[sort_s].append(s)

        return list(d.values())

    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s, map_t = {}, {}
        
        for i in range(len(s)):
            map_s[s[i]] = map_s.get(s[i], 0) + 1
            map_t[t[i]] = map_t.get(t[i], 0) + 1
        
        return map_s == map_t