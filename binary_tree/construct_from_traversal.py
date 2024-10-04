from . import TreeNode
from .traversal import pre_order, post_order, in_order

def construct_from_inorder_preorder(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """
    Build a binary search tree given the output of its in-order and pre-order traversals
    """
    # this approach uses a more optimized way of getting the index of the root using a hashmap
    inorder_frequency = dict()

    for idx, val in enumerate(inorder):
        inorder_frequency[val] = idx
    

    def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # no root for empty traversals
        if not preorder or not inorder:
            return None
        
        # the root is given as the first element in a preorder traversal
        root = TreeNode(preorder[0])
        # now the position can be retrieved in O(1) time
        root_position = inorder_frequency[preorder[0]]

        # elements to the left of the root form the left subtree in an inorder traversal
        root.left = build_tree(preorder=preorder[1:root_position + 1], inorder=inorder[:root_position])
        root.right = build_tree(preorder=preorder[root_position + 1:], inorder=inorder[root_position + 1:])

        return root

    return build_tree(preorder=preorder, inorder=inorder)

if __name__ == "__main__":
    inorder = [4, 8, 10, 12, 14, 20, 22]
    preorder = [20, 8, 4, 12, 10, 14, 22]

    root = construct_from_inorder_preorder(preorder=preorder, inorder=inorder)
    pre_order(root)