class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        stack1 = []
        stack2 = []
        while stack1 or stack2 or root1 or root2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left
            if not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val):
                node = stack1.pop()
                res.append(node.val)
                root1 = node.right
            else:
                node = stack2.pop()
                res.append(node.val)
                root2 = node.right
        return res