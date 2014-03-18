__author__ = 'song.yang'

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def _preOrder(self, root):
        pass


    def hasPathSum(self, root, sum):
        self._sum = root.val
        if root.left:
            self._sum += _preOrder(root.left)
        elif root.right:
            self._sum += _preOrder(root.right)



