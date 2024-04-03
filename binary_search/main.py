def binary_search ( nums: list[int], target: int) -> int:
    # list needs to be sorted in order to perform binary search
    # define left and right pointers
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        guess = nums[mid]
        if (target == guess):
            return mid
        if(target < guess):
            right = mid - 1
            continue
        if (target > guess):
            left = mid + 1
            continue
    return None

my_list = [1, 2, 3, 4, 5]
print(binary_search(my_list, 1))

        