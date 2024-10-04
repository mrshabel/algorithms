from . import TreeNode

def pre_order(root: TreeNode):
    """
    Perform a pre-order traversal on a given binary search tree
    """
    if not root:
        return
    
    # process root
    print(root.val)

    # process left subtree
    pre_order(root.left)

    # process right subtree
    pre_order(root.right)

def in_order(root: TreeNode):
    """
    Perform an in-order traversal on a given binary search tree
    """
    if not root:
        return
    
    # process left subtree
    in_order(root.left)

    # process root
    print(root.val)

    # process right subtree
    in_order(root.right)


def post_order(root: TreeNode):
    """
    Perform a post-order traversal on a given binary search tree
    """
    if not root:
        return
    
    # process left subtree
    post_order(root.left)

    # process right subtree
    post_order(root.right)

    # process root
    print(root.val)