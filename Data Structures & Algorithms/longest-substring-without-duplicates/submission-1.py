class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # char:last_index map
        l, length = 0, 0

        for r in range(len(s)):
            if s[r] in char_map:
                # When a character repeats, 
                # the earliest valid starting point 
                # moves to one position after its previous occurrence.
                l = max(char_map[s[r]] + 1, l)
            
            char_map[s[r]] = r
            length = max(length, r - l + 1)
        
        return length