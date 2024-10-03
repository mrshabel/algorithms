from . import TreeNode
from .traversal import pre_order, in_order

def create_minimal_bst(nums: list[int]) -> TreeNode:
    """
    Given an array of increasing integers ```nums```, return the root of the binary search tree created with minimal height
    """

    # recursively construct the binary search tree from the left and right subtrees by using the middle element as the root node, elements left to mid as left subtree and elements right to mid as right subtree
    def dfs(nums: list[int], start: int, end: int) -> TreeNode:
        if end < start:
            return None
        
        mid = (start + end) // 2

        # set root to middle node
        root = TreeNode(nums[mid])

        root.left = dfs(nums=nums, start=start, end=mid - 1)
        root.right = dfs(nums=nums, start=mid + 1, end=end)

        # return the root for subsequent recursive steps
        return root
    
    return dfs(nums=nums, start=0, end=len(nums) - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]

    result = create_minimal_bst(nums=nums)
    pre_order(result)
