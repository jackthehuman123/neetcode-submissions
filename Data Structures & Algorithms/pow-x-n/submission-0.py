class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = x
        if n > 0:
            for _ in range(n - 1):
                res *= x
        elif n < 0:
            for _ in range(-n - 1):
                res *= x
        else:
            res = 1 
        if n < 0:
            res = 1 / res
        return res