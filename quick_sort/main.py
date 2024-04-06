from random import randint
# quick sort choosing the middle element as the pivot
def quick_sort(nums: list[int]) -> list[int]:
    # define base case
    if len(nums) < 2:
        return nums
    
    # to always result in an average case of runtime complexity, we choose a random index as our pivot
    pivot = nums[randint(0, len(nums) - 1)]
    less, greater = [i for i in nums if i < pivot], [i for i in nums if i > pivot]

    # call quick sort recursively
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([2, 4, 10, 7, 3, 1]))