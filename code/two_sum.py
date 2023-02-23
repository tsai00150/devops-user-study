def twoSum(nums: list, target: int):
    # 0
    # d = {}
    # for i in range(len(nums)):
    #     d[nums[i]] = i

    # for i in range(len(nums)):
    #     if target-nums[i] in d:
    #         return [i, d[target-nums[i]]]
    
    # 1
    # d = {}
    # for i in range(len(nums)):
    #     d[nums[i]] = i

    # for i in range(len(nums)):
    #     if target-nums[i] in d:
    #         return [i, d[target-nums[i]]]
    # return [-1]

    # 2
    # d = {}
    # for i in range(len(nums)):
    #     if target-nums[i] in d:
    #         return [d[target-nums[i]], i]
    #     d[nums[i]] = i
    # return [-1]

    # 3
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