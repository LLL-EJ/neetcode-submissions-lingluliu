class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        
        for char in s:
            if char not in s_map.keys():
                s_map[char] = 1
            s_map[char] += 1

        for char in t:
            if char not in t_map.keys():
                t_map[char] = 1
            t_map[char]+= 1
        
        return s_map == t_map