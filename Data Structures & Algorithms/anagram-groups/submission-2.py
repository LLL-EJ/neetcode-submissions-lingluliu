class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for t in s:
                count[ord(t) - ord('a')] += 1
            
            d[tuple(count)].append(s)
        
        return list(d.values())