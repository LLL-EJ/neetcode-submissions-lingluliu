class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        maxf, l = 0, 0

        for r in range(len(s)):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            maxf = max(maxf, mp[s[r]])
            cur_window_size = r - l + 1

            if cur_window_size - maxf > k:
                mp[s[l]] -= 1
                l += 1
        return r - l + 1