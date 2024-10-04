def max_sub_array_sum(nums: list[int]) ->int:
    """
    Return the maximum sum of a contiguous sub-array in a given array
    This solution uses Kadane's algorithm
    """
    max_sum = nums[0]
    current_sum = nums[0]

    right = 1
    
    while right < len(nums):
        # reset when current sum is negative
        if current_sum < 0:
            current_sum = 0
        current_sum += nums[right]
        right += 1
        max_sum = max(max_sum, current_sum)
    
    return max_sum


if __name__ == "__main__":
    # the right pointer starts from the first element and iterates through the array while accumulating the sum. when the sum is negative, a reset occurs where the accumulated sum is set to 0
    nums = [2, 3, -8, 7, -1, 2, 3]
    result = max_sub_array_sum(nums)

    print(result)


