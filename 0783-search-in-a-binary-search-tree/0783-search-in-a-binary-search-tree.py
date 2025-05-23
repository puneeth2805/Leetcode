# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack=[root]
        while stack:
            node=stack.pop()
            if node.val==val:
                return node
            elif node.val<val and node.right:
                stack.append(node.right)
            elif node.val>val and node.left:
                stack.append(node.left)
        return None
        