class Solution:
    def climbStairs(self, n: int) -> int:
        #if n<=2: return n
        #return self.climbStairs(n-1) + self.climbStairs(n-2)
        s = {}
        s[0] = 1
        s[1] = 2
        for i in range(2, n):
            s[i] = s[i-1] + s[i-2]
        return s[n-1]
        """
        if n<=2: return n
        a, b, res = 1, 2, 0
        for i in range(2, n):
            res = a + b
            a = b
            b = res
        return res
        """
            
