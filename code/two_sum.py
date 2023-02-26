def twoSum(nums: list, target: int):
    d = {}
    for i in range(len(nums)):
        d[nums[i]] = i

    for i in range(len(nums)):
        if target-nums[i] in d:
            return [i, d[target-nums[i]]]
