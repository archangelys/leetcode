__author__ = 'song.yang'

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        newlist = [a for a in A if a != elem]
        newlist.a
        return len(newlist)

if __name__ == '__main__':
    s = Solution()
    A = [4,5,4,6,4,7,4,8]
    print s.removeElement(A,4)

