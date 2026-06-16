class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N = len(s)
        l,r = 0, 0
        bl,br = 0,0

        have, needed = 0,0
        window = {}
        need = {}
        for c in t:
            if c not in need:
                need[c] = 1
                window[c] = 0
                needed += 1
            else:
                need[c] += 1

        for i in range (N):
            # if in need
            if s[i] in need:
                window[s[i]] += 1
                if window[s[i]] == need[s[i]]:
                    have += 1
                    if have == needed:
                        r = i + 1

            
            # Shrink window
            while have == needed:
                # Update the best window 
                dist = (r-l)
                best = (br -bl)
                if dist <  best or best == 0: 
                    br = r
                    bl = l
                # Move left pointer
                if s[l] in window:
                    window[s[l]] -=1 
                    if window[s[l]] < need[s[l]]:
                        have -= 1
                l += 1 
                    
        print(bl, br)
        return s[bl:br]

