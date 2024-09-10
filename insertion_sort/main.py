def insertion_sort(nums: list) -> list:
    """
    Perform an insertion sort on a list of numbers

    ```Notes```: In the event of the array being unsorted and descending, the inner loop runs: 1, 2, 3, 4... which translates to an equivalence of n * n 
    """
    # first element is assume sorted
    for i in range(1, len(nums)):
        # start from element at index 1, then compare to preceding numbers
        j = i - 1

        # swap if j + 1 is less than j and decrement j
        while j >= 0 and nums[j + 1] < nums[j]:
            # swap
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp

            # decrement j to check for other preceding values
            j -= 1
    
    return nums

if __name__ == "__main__":
    nums = [4, 3, 2, 1]
    output = insertion_sort(nums)
    print(output)