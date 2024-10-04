from . import TreeNode

def construct_from_inorder_preorder(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """
    Build a binary search tree given the output of its in-order and pre-order traversals
    """
    # no root for empty traversals
    if not preorder or not inorder:
        return None
    
    # the root is given as the first element in a preorder traversal
    root_position = preorder[0]
    root = TreeNode(preorder[root_position])

    # elements to the left of the root form the left subtree in an inorder traversal
    root.left = construct_from_inorder_preorder(preorder=inorder[:root_position], inorder=inorder[:root_position])
    root.right = construct_from_inorder_preorder(preorder=inorder[root_position + 1:], inorder=inorder[root_position + 1:])

    return root

if __name__ == "__main__":
    inorder = [4, 8, 10, 12, 14, 20, 22]
    preorder = [20, 8, 4, 12, 10, 14, 22]