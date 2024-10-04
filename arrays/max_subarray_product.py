def max_sub_array_product(nums: list[int]) ->int:
    """
    Return the maximum product of a contiguous sub-array in a given array
    """
    current_max = current_min = res = nums[0]

    for num in nums:
        # swap current minimum and maximum when a negative number is encountered
        # the swap is due to the fact that the product of a large integer and a negative integers results in a smaller value, hence use the current_min to get a negative value much closer to 0
        if num < 0:
            temp = current_min
            current_min = current_max
            current_max = temp
        
        # update the maximum and minimum product
        current_max = max(current_max * num, num)
        current_min = min(current_min * num, num)

        res = max(res, current_max)
    
    return res

if __name__ == "__main__":
    nums = [-2, 6, -3, 10, 0, 2]
    result = max_sub_array_product(nums)

    print(result)


