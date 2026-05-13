class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # res = []s

        res = set([])

        def dfs(l : int, r : int, para : str):
            # Base case
            if l == 0 and r == 0:
                res.add(para)

            # Can add left para
            if l > 0:
                # para += "("
                # l -= 1

                dfs(l-1, r, para+"(")
            
             # Add right para
            if r > l:
                # para += ")"
                # r -= 1
                dfs(l, r-1, para+")")
            

        dfs(n, n, "")

        return list(res)