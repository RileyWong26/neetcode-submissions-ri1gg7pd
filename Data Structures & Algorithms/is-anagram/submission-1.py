class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {

        }

        # Add to hash containing num characters in s
        for c in s:
            if c not in hash:
                hash[c] = 1
            else:
                hash[c] += 1

        # remove from hash
        for c in  t:
            # If not in hash not same
            if c not in hash:
                return False
            else: 
                # Decrease counter
                hash[c] -= 1
                if hash[c] == 0:
                    hash.pop(c)
        return len(hash) == 0

        
