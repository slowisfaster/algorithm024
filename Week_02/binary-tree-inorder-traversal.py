class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
	#中序
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
	#前序
	return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

