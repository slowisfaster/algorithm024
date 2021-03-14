class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix)<1: return 0
        r = len(matrix)
        c = len(matrix[0])
        dp = [[0] * (c + 1) for _ in range(r + 1)]
        m = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
                    m = max(m, dp[i+1][j+1])
        return m * m

