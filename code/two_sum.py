def twoSum(nums: list, target: int):
    if (not nums or len(nums) == 1):
        return
    d = dict()
    for i in range(len(nums)):
        d[nums[i]] = i
    
    for each in d:
        diff = target - each
        if diff in d.keys():
            return [d[each], d[diff]]

nums = []
target = 9