def twoSum(nums: list, target: int):
    d = dict()
    for i in range(len(nums)):
        d[nums[i]] = i
    
    for each in d:
        diff = target - each
        if diff in d.keys():
            return [d[each], d[diff]]

nums = [2,7,11,15]
target = 9