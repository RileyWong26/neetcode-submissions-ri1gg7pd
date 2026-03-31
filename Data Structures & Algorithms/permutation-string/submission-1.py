class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Create hash
        hash = {}

        for c in s1:
            if c not in hash:
                hash[c] = 1
            elif c in hash:
                hash[c] += 1
        numC = len(hash)

        if len(s2) < len(s1):
            return False
        # Create sliding window
        for i in range(0, len(s1)):
            if s2[i] in hash:
                hash[s2[i]] -= 1
                if hash[s2[i]] == 0:
                    numC -= 1
            

        if numC == 0:
                return True

        # Add the left most character to the hash when shifting the sliding window

        for i in range(len(s1), len(s2)):
            # if the element being moved out of the window is in the hash add it back
            if s2[i-len(s1)] in hash:
                if hash[s2[i-len(s1)]] == 0:
                    numC +=1
                hash[s2[i-len(s1)]] += 1
                    
            if s2[i] in hash:
                hash[s2[i]] -= 1
                if hash[s2[i]] == 0:
                    numC -= 1
            if numC == 0:
                return True
        return False
        