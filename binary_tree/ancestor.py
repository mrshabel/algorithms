from . import TreeNode
from .insert_bst import insert_bst
from .traversal import pre_order, in_order, post_order

def lowest_common_ancestor(root: TreeNode | None, p: int, q: int) -> int | None:
    """
    Find the lowest common ancestor of two given nodes.
    ```Runtime analysis```: The properties of a bst as used in this case ensures than we recursively branch to a subtree, and hence, O(h)
    """
    # no ancestor for an empty tree
    if not root:
        return None
    
    # the cases to handle: if both nodes are lesser than current node, process left subtree, if both nodes are greater than current node, process right subtree
    if p < root.val and q < root.val:
        return lowest_common_ancestor(root.left, p, q)
    elif p > root.val and q > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    # last case for when either one or both nodes equal the current node, thus the common ancestor
    return root.val


if __name__ == "__main__":
    values = [8, 4, 12, 10, 14, 22]
    root = TreeNode(20)

    for val in values:
        node = TreeNode(val)
        insert_bst(root, val)
    print(pre_order(root))
        
    result1, result2 = lowest_common_ancestor(root=root, p=10, q=14), lowest_common_ancestor(root=root, p=8, q=14)
    print(f"Ancestor or 10 and 14: {result1}\nAncestor of 8 and 14: {result2}")