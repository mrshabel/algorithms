def merge_sort(nums: list[int]) -> list[int]:
    """
    Sort a list of integers using merge sort algorithm
    """
    # base case for when length of array is 1
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2

    # recursively run merge sort on two halves
    left = merge_sort(nums[:mid]) # 0 to mid - 1
    right = merge_sort(nums[mid:]) # mid to end of nums

    # merge left and right halves of the array

    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    """
    Merge the right and left halves of an array
    """
    merged = []
    # define 2 pointers i and j
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # add remaining elements in either lists
    if i < len(left):
        merged += left[i:]
    if j < len(right):
        merged += right[j:]
    
    return merged


if __name__ == "__main__":
    nums = [5, 4, 3, 2, 1]
    result = merge_sort(nums)
    print(result)