from . import TreeNode
from .insert_bst import insert_bst

def check_balanced(root: TreeNode | None) -> bool:
    """
    Check if a binary tree is balanced or not
    """

    def dfs(root: TreeNode | None):
        # base case for empty tree
        if not root:
            return [True, 0]
        
        # get height difference between subtrees
        left, right = dfs(root.left), dfs(root.right)
        
        # check if tree is balanced from root, left, right subtrees are balanced
        balanced = abs(left[1] - right[1]) <= 1 and (left[0] and right[0])

        # return incremented height
        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]



if __name__ == "__main__":
    values = [1, 2, 4, 5, 6]
    root = TreeNode(3)

    for val in values:
        node = TreeNode(val)
        insert_bst(root, val)

    result = check_balanced(root=root)
    print(result)
    
