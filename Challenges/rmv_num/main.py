def remove_nonints(nums):
    only_int = []
    for num in nums:
        if type(num) == int:
            only_int.append(num)
    return only_int