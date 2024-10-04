def max_area_of_container(nums: list[int]) -> int:
    """
    Return the maximum area formed in the container covered by water
    """
    # by using a sliding window approach, the breadth is shifted depending on the side with less height
    left, right = 0, len(nums) - 1
    area = 1

    while left <= right:
        distance = right - left
        # use the min height here to avoid overflow of water in the container
        min_height = min(nums[left], nums[right])

        if nums[left] <= nums[right]:
            left += 1
        else:
            right -= 1

        area = max(area, distance * min_height)
    
    return area


if __name__ == "__main__":
    nums = [1, 5, 4, 3]
    result = max_area_of_container(nums)
    
    print(result)