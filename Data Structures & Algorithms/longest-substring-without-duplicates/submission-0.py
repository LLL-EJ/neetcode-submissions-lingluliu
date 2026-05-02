class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        length, l = 0, 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            length = max(length, r - l + 1)

        return length
            
           
                
            