class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(start, end, target):
            mid = (end - start ) // 2 + start 
            # FOund
            if nums[mid] == target:
                return mid

            # Base case not found 
            if start == end: 
                return -1  

            if nums[mid] > target: 
                return bin_search (start, mid, target)
            return bin_search(mid +1, end , target)

        
        return bin_search(0, len(nums) - 1, target)
            
        