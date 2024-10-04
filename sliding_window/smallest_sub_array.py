def smallest_sub_array(nums: list[int], target: int) -> int:
    """
    Find the length of the smallest sub-array whose sum is greater than or equal to ```target```
    """
    # define two pointers
    left, right = 0, 0
    current_sum = 0
    min_length = len(nums)


    while right < len(nums):
        # expand current sub-array with right pointer util target is reached
        if current_sum < target:
            current_sum += nums[right]

        while current_sum >= target:
            # calculate minimum length and shrink the sub-array to find a minimum size
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
        
        right += 1

    return min_length


if __name__ == "__main__":
    nums = [4, 2, 2, 7, 8, 1, 2, 8, 10]

    result = smallest_sub_array(nums, 8)
    print(result)