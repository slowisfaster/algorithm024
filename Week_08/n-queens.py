class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, xy_dif, xy_sum):
            r = len(queens)
            if r == n:
                result.append(queens)
                return
            for c in range(n):
                if c not in queens and r-c not in xy_dif and r+c not in xy_sum:
                    dfs(queens+[c], xy_dif+[r-c], xy_sum+[r+c])
        result = []
        dfs([],[],[])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in result]
