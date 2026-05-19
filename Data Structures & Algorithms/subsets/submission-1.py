class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(pos: int, sub: list):
            # Base case out of bounds
            if pos >= len(nums):
                res.append(sub)
                return

            # Choose to add
            sub.append(nums[pos])
            dfs(pos + 1, sub.copy())

            # Choose to ignore
            sub.pop(-1)
            dfs(pos + 1, sub.copy())            


        res = []

        dfs(0, [])

        return res