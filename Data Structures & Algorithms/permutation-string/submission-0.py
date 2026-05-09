class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26  # index mapping 0 -> 25 : a-z -> frequent count for a-z
        window_count = [0] * 26

        # check the 1st window in s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            window_count[ord(s2[i]) - ord("a")] += 1

        if s1_count == window_count:
            return True

        # check the rest windows in s2

        for i in range(len(s1), len(s2)):
            # shift the window, add next char in s2
            new_char = s2[i]
            window_count[ord(new_char) - ord("a")] += 1
            # remove the first char from the window
            old_char = s2[i - len(s1)]
            window_count[ord(old_char) - ord("a")] -= 1
        
            if s1_count == window_count:
                return True
        
        return False