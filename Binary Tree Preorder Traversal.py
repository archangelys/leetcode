__author__ = 'song.yang'
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        order = []
        self._traver(root,order)


    def _traver(self, node, order):
        if node.left:
            order = self._traver(node.left, order)
        order.append(node.val)
        if node.right:
            self._traver(node.right, order)