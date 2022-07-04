def sum_all(nums):
    total = 0
    for num in nums:
        if type(num) == list:
            total += sum_all(num)
        else:
            total += num

    return total

#