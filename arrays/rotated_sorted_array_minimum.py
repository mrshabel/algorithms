def rotated_sorted_array_minimum(nums: list[int]) ->int:
    """
    Return the minimum element in a sorted array rotated at an unknown point
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        # early return if array is already sorted
        if nums[left] <= nums[right]:
            return nums[left]
            
        mid = (left + right) // 2

        # search right space
        if nums[mid] > nums[right]:
            left = mid + 1
        # search left space but start from the midpoint exactly as mid could be the least element
        elif nums[mid] < nums[right]:
            right = mid
        else:
            return nums[mid]
    
    return -1

if __name__ == "__main__":
    nums = [5, 6, 1, 2, 3, 4]
    result = rotated_sorted_array_minimum(nums)

    print(result)


