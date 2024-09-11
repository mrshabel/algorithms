from . import TreeNode

def can_reach_leaf(root: TreeNode | None) -> bool:
    """
    Determine if a path exists from the root of a tree to a leaf node where no node contains zero(0)
    """
    # base case for when a null node is reached or value of node is zero
    if not root or root.val == 0:
        return False
    
    # determine if node is a leaf
    if not root.left and not root.right:
        return True
    
    # recursively check for left and right subtree
    if can_reach_leaf(root.left):
        return True
    if can_reach_leaf(root.right):
        return True
    
    return False