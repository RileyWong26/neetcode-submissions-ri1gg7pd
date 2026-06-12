class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # c : i ; where c is hte character and i is the position in the window 
        window = {}

        N = len(s)
        l,r = 0,0
        longest = 0
        res = 0

        for i in range(N):
            # In the window already
            if s[i] in window and window[s[i]] >= l:
                
                res = max(res, r-l )
                l = window[s[i]]+ 1
                r = i+1
                window[s[i]] = i

            # Not in the window
            else:
                r = i+1
                window[s[i]] = i
        return max(res, r-l)
