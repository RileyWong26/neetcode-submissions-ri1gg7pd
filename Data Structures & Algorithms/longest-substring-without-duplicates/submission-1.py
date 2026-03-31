class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        length = 0

        for c in s:
            if c in sub:
                sub = sub[sub.find(c) + 1:]
                sub += c
            else:
                sub += c
            length = max(len(sub), length)
        
        return length
            
