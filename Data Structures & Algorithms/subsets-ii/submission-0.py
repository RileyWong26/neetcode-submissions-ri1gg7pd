class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:   
        nums.sort()

        def dfs(pos, inp):
            # Base case
            if pos >= len(nums):
                res.append(inp)
                return

            # ADD
            tmp = inp.copy()
            tmp.append(nums[pos])
            dfs(pos + 1, tmp)

            # Skip
            curr = nums[pos]
            while pos < len(nums) and nums[pos] == curr:
                pos += 1
            cpy = inp.copy()
            # cpy.pop(-1)
            dfs(pos, cpy)
 
        res = []
        dfs(0, [])

        return res