__author__ = 'song.yang'

# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# For example:
# Given array A = [2,3,1,1,4]

# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        current = 0; maxpos = 0; step = 0;

        if n <= 1:
            return step

        while current <= maxpos:
            step += 1
            nextpos = maxpos + 1
            for i in range(current, nextpos):
                if A[i] + i > maxpos:
                    maxpos = A[i] + i
                    if maxpos >= n - 1:
                        return step
            current = nextpos

        return -1
