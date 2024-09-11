class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left: TreeNode  | None = left
        self.right: TreeNode | None = right