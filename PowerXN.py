__author__ = 'song.yang'

# AC
# Todo Haven't fully understand
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        result = 1
        negetive = False
        if n < 0:
            n = -n
            negetive = True
        while n:
            if n%2 :
                result *= x
            x *= x
            n /= 2
        return 1/result if negetive else result