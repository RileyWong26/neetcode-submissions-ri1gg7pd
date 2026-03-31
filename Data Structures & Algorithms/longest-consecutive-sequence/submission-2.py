class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Hash to store whats in the array
        hash = {}

        # Add all unique elements to the hash
        for num in nums:
            if num not in hash:
                hash[num] = 1
        
        # Sort keys
        sortedkeys = sorted(hash.keys())
        if len(sortedkeys) == 0:
            return 0
        length = 1
        highest = 0
        for i in range(1, len(sortedkeys)):
            # if 1 greater than the previous
            if sortedkeys[i] == sortedkeys[i - 1] + 1:
                length += 1
            # Else try new sequence and take maximum of last 
            else:
                highest = max(highest, length)
                length = 1

        highest = max(highest, length)
        return highest