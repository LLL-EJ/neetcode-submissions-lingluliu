class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window, count_t = {}, {}
        # count map for string t
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        # we need have (window contains all chars in t) >= need (len of unique chars in t)
        have, need = 0, len(count_t) #-> unique values without duplicates
        res = [-1, -1]
        len_res = float("infinity")
        l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1
            
            while have == need:
                # update result once the current window size (r - l + 1) is less than the current length of substring
                if (r - l + 1) < len_res:
                    res = [l, r]
                    len_res = r - l + 1
                
                # shrink the substring to find the min
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l : r + 1] if len_res != float("infinity") else ""