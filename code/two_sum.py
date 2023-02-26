def twoSum(nums: list, target: int):
    for i in range(len(nums)):
        if type(nums[i]) != int:
            try:
                nums[i] = int(nums[i])
            except:
                return [-1]

    d = {}
    for i in range(len(nums)):
        if target-nums[i] in d:
            return [d[target-nums[i]], i]
        d[nums[i]] = i
    return [-1]
twoSum([2,7,11,15],9)
