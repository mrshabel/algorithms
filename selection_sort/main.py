

def selection_sort(nums: list[int]) -> list[int]:
    sorted_nums = []
    while len(nums) > 0:
        for i in range(len(nums)):
            smallest_index = 0
            if nums[i] < nums[smallest_index]:
                smallest_index = i
        sorted_nums.append(nums.pop(smallest_index))
    return sorted_nums
            


print(selection_sort([2, 5, 4, 3]))
            