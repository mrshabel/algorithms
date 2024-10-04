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
# print(binary_search(my_list, 1))

def recursive_binary_search(nums: list[int], target: int):

    def search(start: int, end: int):
        # base case for when target is not present
        if end < start:
            return -1
        
        mid = (start + end) // 2

        # base case for when target is found
        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            return search(start=start, end=mid - 1)
        elif target > nums[mid]:
            return search(start=mid + 1, end=end)
    
    return search(start=0, end=len(nums) - 1)
        

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]

    result = recursive_binary_search(nums=nums, target=5)
    print(result)