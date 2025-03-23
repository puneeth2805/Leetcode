# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxTill):
            if not root:
                return 0
            if root.val>=maxTill:
                good=1
            else:
                good=0
            new_max=max(maxTill,root.val)
            return good+dfs(root.left,new_max)+dfs(root.right,new_max)
        return dfs(root,float('-inf'))
        