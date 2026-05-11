class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 2 options, not add, add
        
        res = []

        candidates.sort()
        
        def dfs(pos, arr, total):
            # Base case: gone through all candidates
            if pos == len(candidates) or total > target:
                return 

            if total == target:
                res.append(arr.copy())
                return 

            # Decide to skip current position
            c = pos 
            while c <= len(candidates) -1 and candidates[c] == candidates[pos]:
                c += 1 
            if c <= len(candidates) -1:
                dfs(c, arr.copy(), total)
            
            # Add the current position
            arr.append(candidates[pos])
            total += candidates[pos]
            
            # Base case: sum is target
            if total == target:
                res.append(arr)
                return
            
            dfs(pos + 1, arr.copy(), total)

        dfs(0, [], 0)

        return res
