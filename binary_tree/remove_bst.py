from . import TreeNode
from .insert_bst import insert_bst
from .traversal import pre_order

def find_minimum_node(root: TreeNode) -> TreeNode:
    """
    Find the node with the minimum value in a binary search tree
    """
    current = root
    # branch to the left subtree as all nodes with minimum values are on the left subtree
    while current and current.left:
        current = current.left
    
    return current

def remove_bst(root: TreeNode | None, val: int) -> TreeNode:
    """
    Remove a node from a binary search tree
    """
    # two cases: when the node has no or one child and when it has 2 children
    # if the node has two children, replace it with the lowest leaf node in the right subtree, or largest value in left subtree

    # base case: return null when node is removed
    if not root:
        return None
    
    # traverse left subtree if val is lesser than value of node
    if val < root.val:
        root.left = remove_bst(root.left, val)
    # traverse right subtree if val is greater than value of node
    elif val > root.val:
        root.right = remove_bst(root.right, val)
    # finally perform checks when node is found
    else:
        # handle case 1 where node has one or no child, return non-null child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        # handle case 2 where node has 2 children
        else:
            # find the minimum node in the right subtree and replace the root node's value with it
            min_node = find_minimum_node(root.right)
            root.val = min_node.val
            # recursively delete the minimum node found and assign subtree to root
            root.right = remove_bst(root.right, min_node.val)
    
    # return root to preserve integrity otherwise changes made would be lost
    return root

if __name__ == "__main__":
    values = [1, 2, 4, 5]
    root = TreeNode(3)

    for val in values:
        node = TreeNode(val)
        insert_bst(root, val)
    
    remove_bst(root, 3)
    pre_order(root)