def bubble_sort(nums: list[int]) -> list[int]:
    """
    Sort a list of numbers using bubble sort

    ```Detail```: the largest element in the list is placed at its final position at the end of each iteration. 
                A ```swapped``` variable is used to avoid redundant checks, thereby maintaining a best case of O(n)
    """
    # initialize swapped to false
    swapped = False

    for left in range(len(nums)):
        # swap adjacent elements until last sorted element is reached, thus, (len(nums) - left - 1)
        for right in range(0, len(nums) - left - 1):
            if nums[right] > nums[right + 1]:
                temp = nums[right]
                nums[right] = nums[right + 1]
                nums[right + 1] = temp

                swapped = True
            
        # if no swap has ocurred then nums is already sorted
        if not swapped:
            break
    
    return nums
    


if __name__ == "__main__":
    nums = [5, 4, 3, 2, 1]
    result = bubble_sort(nums)
    print(result)