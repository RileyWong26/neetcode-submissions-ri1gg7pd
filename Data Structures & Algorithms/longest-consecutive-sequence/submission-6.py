class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = {}
        if len(nums) == 0:
            return 0
        for n in nums:
            hash[n] = 1
        
        res = 0
        length = 0
        

        
        for key in hash.keys():
            while key + length in hash:
                length +=1
            res = max(res, length)
            length =0

        return res