def majority_number(nums):
    if not nums:
        return None

    cand, count = None, 0
    for num in nums:
        if count == 0:
            cand, count = num, 1
        elif num == cand:
            count += 1
        else:
            count -= 1

    return cand