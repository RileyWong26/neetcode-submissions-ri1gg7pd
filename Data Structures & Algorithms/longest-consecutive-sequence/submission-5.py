class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = {}
        if len(nums) == 0:
            return 0
        for n in nums:
            hash[n] = 1
        
        res = 0
        length = 0
        
        mx = max(nums)
        mn = min(nums)

        for i in range(mn,mx + 1):
            if i in hash: 
                length += 1 
            
            else:
                res = max(res, length)
                length = 0

        res = max(res, length)
        return res