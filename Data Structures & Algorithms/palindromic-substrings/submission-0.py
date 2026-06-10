class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0 

        # Odd palindromes
        for i in range(N):
            l,r = i,i
            res += 1

            # Expand outwards
            while l > 0 and r < N-1:
                l -= 1
                r += 1
                if s[l] == s[r]:
                    res += 1
                else:
                    break
            

        # Even palindromes
        for i in range(N-1):
            l, r = i, i+1
            
            while l >=0 and r<= N-1:
                if s[l] == s[r]:
                    res+= 1
                else:
                    break
                l-=1
                r+=1


        return res