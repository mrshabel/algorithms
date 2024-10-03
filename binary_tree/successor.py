from . import TreeNode
from .insert_bst import insert_bst

def find_successor(root: TreeNode | None, target: int):
    """
    Find the in-order successor of a given node
    """
    # for empty trees, there are no successors
    if not root:
        return None
    
    # if target is less than node, process left subtree
    if target < root.val:
        find_successor(root.left, target)
    elif target > root.val:
        # process right subtree
        find_successor(root.right, target)
    else:
        # process when the found node is the target
        
        # handle case where right subtree is present
        if root.right:
            node = find_minimum(root.right)
            return node.val

def find_minimum(node: TreeNode):
        """
        Find the minimal node in a given bst
        """
        if not node:
            return None
        
        current = node
        while current and current.left:
            current = current.left
        
        return current


if __name__ == "__main__":
    values = [30, 20, 40, 70, 60, 80]
    root = TreeNode(50)

    for val in values:
        node = TreeNode(val)
        insert_bst(root, val)
    
    result = find_successor(root=root, target=50)
    print(result)