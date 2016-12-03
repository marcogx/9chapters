def single_number(nums):
    if not nums:
        return None

    res = nums[0]
    for i in xrange(1, len(nums)):
        res ^= nums[i]

    return res
