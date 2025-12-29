class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.prev = None

        def preorder(node):
            if not node:
                return
            preorder(node.right)
            preorder(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node

        preorder(root)
