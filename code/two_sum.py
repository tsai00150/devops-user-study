def twoSum(nums: list, target: int):
    dictionary = {}
    
    for i in range(0,len(nums)):
        if nums[i] in dictionary:
            dictionary[nums[i]].append(i)
        else:
            dictionary[nums[i]] = [i]

    for i in range(0,len(nums)):
        curr_num = nums[i]
        diff = target - curr_num
        if diff in dictionary:
            return [i, dictionary[diff][0]]
    
    return None