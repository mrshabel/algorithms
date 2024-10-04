def max_sum_sub_array(nums: list[int], length: int) -> int:
    """
    Find the maximum contiguous sum of a fixed sub-array in the given array, ```nums```
    """
    # define left and right pointers
    left, right = 0, length - 1
    max_sum = nums[0]

    while right < len(nums):
        max_sum = max(max_sum, sum(nums[left:right + 1]))
        left += 1
        right += 1
    
    return max_sum



if __name__ == "__main__":
    nums = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]

    result = max_sum_sub_array(nums, 3)
    print(result)
