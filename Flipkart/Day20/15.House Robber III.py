class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            not_rob = max(left) + max(right)
            rob = node.val + left[0] + right[0]
            return [not_rob, rob]
        return max(dfs(root))