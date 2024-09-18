def find_min(nums):
    min_num = float("inf")

    for num in nums:
        if num < min_num:
            min_num = num
    return min_num