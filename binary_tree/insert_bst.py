from . import TreeNode
from .traversal import pre_order

def insert_bst(root: TreeNode | None, val: int) -> TreeNode:
    """
    Insert a node into a binary search tree
    """
    # base case: when the leaf is reached, create a new node and return it
    if not root:
        return TreeNode(val)
    
    # insert into left subtree
    if val < root.val:
        root.left = insert_bst(root.left, val)
    # insert into right subtree
    elif val > root.val:
        root.right = insert_bst(root.right, val)
    
    # return the root
    return root

if __name__ == "__main__":
    root = TreeNode(3)
    insert_bst(root, 1)
    insert_bst(root, 2)
    insert_bst(root, 4)
    insert_bst(root, 5)

    pre_order(root)