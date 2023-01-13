class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.output = 0
        def recur(root):
            if root:
                left_count, left_s = recur(root.left)
                right_count, right_s = recur(root.right)
                avg = (left_s + right_s + root.val) // (left_count + right_count + 1)
                if root.val == avg:
                    self.output += 1
                return left_count + right_count + 1, left_s + right_s + root.val
            return 0, 0
        recur(root)
        return self.output