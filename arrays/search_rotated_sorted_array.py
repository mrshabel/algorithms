def search_rotated_sorted_array(nums: list[int], target: int) ->int:
    """
    Return the the index of a given element element in a sorted array rotated at an unknown point
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        # if middle value is less than or equal to the leftmost value, the leftmost elements are in the left sorted portion
        # when left half is sorted
        if nums[left] <= nums[mid]:
            # process if target is between left and mid
            if target >= nums[left] and target <= nums[mid]:
                right = mid - 1
            # when target is out of bounds in left sorted array
            else:
                left = mid + 1

        # when right half is sorted
        else:
            # when target is between mid and right
            if target >= nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1 
    
    return -1

if __name__ == "__main__":
    nums = [4, 4, 5, 6, 7, 0, 1, 2]
    result = search_rotated_sorted_array(nums, 4)

    print(result)


