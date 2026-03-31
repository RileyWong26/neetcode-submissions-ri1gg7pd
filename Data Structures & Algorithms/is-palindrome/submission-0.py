class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1

        valid = 'ABCDEFGHIJKMLNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        while p1 <= p2:
            if s[p1] not in valid:
                p1 += 1
            if s[p2] not in valid:
                p2 -= 1
            elif s[p2] in valid and s[p1] in valid:
                if s[p2].lower() != s[p1].lower():
                    return False
                p1 += 1
                p2 -=1
            
        return True