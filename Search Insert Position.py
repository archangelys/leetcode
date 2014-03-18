__author__ = 'song.yang'

# AC
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        index = 0
        for ele in A:
            if ele > target or ele == target:
                return index
            index += 1
        return index

